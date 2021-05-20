import json 
import csv
import os,sys
from shapely.geometry import Polygon, Point, MultiPolygon
import pprint
import matplotlib.pyplot as plt
from DBconnect import vic_areas_tweets_db

#Victoria income analyzer 
# def process_area_name(name):
    

class VicAreas:
    def __init__(self,areaName):
        self.name = areaName
        self.average_income = -1
        self.median_age = -1
        self.teenagers_and_young_adults = -1
        self.adults = -1 
        self.middle_age_and_above = -1
        self.density = -1
        self.range =[] # a list of multipolygon



class AurinAnalyzer:
    def __init__(self):
        scriptpath = os.path.dirname(__file__)
        self.incomepath =os.path.join(scriptpath, 'Aurin/income.json')
        self.age_distributionpath = os.path.join(scriptpath, 'Aurin/age_distribution.json')
        self.populationpath =os.path.join(scriptpath, 'Aurin/population.json' )
        self.areas = {}
        print(self.incomepath)
        with open(self.incomepath) as f:
            data = json.load(f)
            statistics = data['features']
            for each in statistics:
                area_name = each['properties']['lga_name_2019']
                income = each['properties']['estimates_personal_income_year_ended_30_june_median_employee']
                area = VicAreas(area_name)
                area.average_income = income
                self.areas[area_name] = area

        with open(self.age_distributionpath) as f:
            data = json.load(f)
            statistics= data['features']
            for each in statistics:
                area_name = each['properties']['lga_name_2019']
                median_age = each['properties']['estmtd_rsdnt_ppltn_smmry_sttstcs_30_jne_mdn_age_prsns_yrs']
                # age 5-19
                teenagers_and_young_adults =  each['properties']['estimated_resident_population_persons_30_june_5_9_years_pc'] + each['properties']['estimated_resident_population_persons_30_june_10_14_years_pc'] +each['properties']['estimated_resident_population_persons_30_june_15_19_years_pc'] 
                #age 20 -40 
                adults = each['properties']['estimated_resident_population_persons_30_june_20_24_years_pc'] + each['properties']['estimated_resident_population_persons_30_june_25_29_years_pc'] + each['properties']['estimated_resident_population_persons_30_june_34_years_pc'] + each['properties']['estimated_resident_population_persons_30_june_35_39_years_pc'] 
                #age 40 -70
                middle_age_and_above = each['properties']['estimated_resident_population_persons_30_june_40_44_years_pc'] + each['properties']['estimated_resident_population_persons_30_june_45_49_years_pc'] + each['properties']['estimated_resident_population_persons_30_june_50_54_years_pc'] + each['properties']['estimated_resident_population_persons_30_june_55_59_years_pc'] 
                self.areas[area_name].median_age = median_age
                self.areas[area_name].teenagers_and_young_adults = teenagers_and_young_adults
                self.areas[area_name].adults = adults
                self.areas[area_name].middle_age_and_above = middle_age_and_above


        with open(self.populationpath) as f:
            data = json.load(f)
            statistics= data['features']
            for each in statistics:
                if each['properties']['state_name_2019'] == "Victoria":
                    area_name = each['properties']['lga_name_2019']
                    geo = each['geometry']['coordinates']
                    density = each['properties']['pop_density_2019_people_per_km2']
                    self.areas[area_name].density = density
                    self.areas[area_name].range = geo

    def store_in_db(self,db = vic_areas_tweets_db):
        print("uploading to db......")
        for key in self.areas:
            area = self.areas[key]
            area_doc = {
                "type": "area",
                "area_name": area.name,
                "average_income": area.average_income,
                "age_distribution": {
                "median_age": area.median_age,
                "teenagers_and_young_adults_ratio": area.teenagers_and_young_adults,
                "adults_ratio": area.adults,
                "middle_age_and_above_ratio": area.middle_age_and_above,

                },
                "population_density":area.density,
                "area_range": area.range
            }

            db[area.name] = area_doc
        print("....uploading data complete")
        

def convert_to_multipolygon(geo):
    multis = []
    for multipoly in geo:
        multi = []
        for poly in multipoly:
            coords = []
            for coord in poly:
                coords.append((coord[0], coord[1]))
            polygon = Polygon(coords)
            multi.append(polygon)
        multis.append(MultiPolygon(multi))

    return multis


def determine_location(areas_dict, coordinates, isBoundingBox = False):
    if not isBoundingBox:
        coord = Point(coordinates[0],coordinates[1] )
        for key in areas_dict:
            ranges = areas_dict[key]
            for each in ranges:
                if each.contains(coord):
                    return key

    else:
        poly = []
        for coord in coordinates:
            poly.append((coord[0], coord[1]))
        poly = Polygon(poly)
        for key in areas_dict:
            ranges = areas_dict[key]
            for each in ranges:
                if each.contains(poly):
                    return key

    return "Out Of Bound" # exceed the range of out chosen analyzed areas 



if __name__ == "__main__":  

    # first time storing the aea data: 
    analyzer = AurinAnalyzer()
    analyzer.store_in_db()


    


