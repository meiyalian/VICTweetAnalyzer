import json
import random

if __name__ == "__main__":

    ## read the twitterAPI file
    twitterJson = open("twitterAPI.json","r")
    data = json.load(twitterJson)
    twitterJson.close()

    ## read the geojson file
    geoJson = open("LGA.geojson","r")
    geoData = json.load(geoJson)
    geoJson.close()
    
    

    for tweet in data["LGA"]:
        for geo in geoData["features"]:

            if tweet["ABB_NAME"] == geo["properties"]["ABB_NAME"]:
                geo["properties"]["sentiment_score"] = tweet["sentiment_score"] 
                geo["properties"]["positive"] = tweet["positive"]
                geo["properties"]["negative"] = tweet["negative"]
                # print(geo["properties"])

    #save data
    newGeo = open("LGA.geojson","w+")
    newGeo.write(json.dumps(geoData))
    newGeo.close()

# #######################
#     for tw in data["LGA"]:
#         tw["age"]=random.randrange(20,80)
#         tw["income"]=random.randrange(30000,55000)
#         print(tw)

#      #save data
#     newt = open("twitterAPI.json","w+")
#     newt.write(json.dumps(data))
#     newt.close()



