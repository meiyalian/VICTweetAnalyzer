# Observatory Service

# Import framework
from flask import Flask
import argparse
import sys
from flask_restful import Resource, Api
from dbSetting import *
import json







app = Flask(__name__)
api = Api(app)


# calculate pos and neg ratio
def calculateRatio(postive, negative):

    total = postive + negative
    pos_ratio = 0
    neg_ratio = 0
    if total  > 0:
        pos_ratio = (postive/total) * 100
        neg_ratio = (negative/total) *100
    return pos_ratio, neg_ratio

#return top n key value pairs in a dict (value is numeric) 
def calculateTop(dictionary, n):
    return sorted(dictionary.items(), key=lambda item: item[1] ,reverse=True)[:n]



class HelloWorld(Resource):
    def get(self):

        return {'hello': 'world'}

api.add_resource(HelloWorld, '/', endpoint = 'hello')


###############  api: /totalCollected
class getVicData(Resource):
    def get(self): 
        return_json = {}
        try:
            collected_result = getStats(RAW_TWEET_DB_NAME, RAW_TWEET_DESIGN_DOC, "getTweetAreaCount")
            analysed_result = getStats(ANALYSIS_DB_NAME, ANALYSIS_DESIGN_DOC, "getTweetAreaCount")
            total_collected = collected_result["rows"][0]["value"]
            total_analysed = analysed_result["rows"][0]["value"]
            return_json = {
                        "ok": True,
                        "data": {
                        "total_collected": total_collected, 
                        "total_analysis": total_analysed}}
        except Exception as e:
            print(e)
            return_json = {
                "ok": False,
                "msg" : "Something went wrong: "}
        return return_json
        
api.add_resource(getVicData, '/totalcollected', endpoint = 'totalcollected')  




###############  api: /incomesentiment


class getIncomeStats(Resource):
    def get(self): 
        return_json = {}

        try:
            income_stats = getStats(RAW_TWEET_DB_NAME, RAW_TWEET_DESIGN_DOC, "getAllAreaIncome")
            area_stats =  getStats(ANALYSIS_DB_NAME, ANALYSIS_DESIGN_DOC, "getStats")["rows"][0]["value"]
 
            areas_dict = {}
            for each in income_stats["rows"]:
                areas_dict[each["key"]] = {"area":each["key"], "positive": 0, "negative": 0 }
                areas_dict[each["key"]]["income_average"] = each["value"] 


            for key in area_stats:
           
                pos_ratio,neg_ratio =  calculateRatio(area_stats[key]["positive"], area_stats[key]["negative"] )
                areas_dict[key]["positive"] = pos_ratio
                
                areas_dict[key]["negative"] = neg_ratio
            data = []
            for key in areas_dict:
                data.append(areas_dict[key])

            return_json = {
                        "ok": True,
                        "data": data}
        except Exception as e:

            print(e)
            return_json = {
                "ok": False,
                "msg" : "Something went wrong: "}
        return return_json
        
api.add_resource(getIncomeStats, '/incomesentiment', endpoint = 'incomesentiment')  




############### api: /topfiveemoji
class getTopFiveEmoji(Resource):
    def get(self): 
        return_json = {}
        emoji_count = {}
        try:
            area_stats =  getStats(ANALYSIS_DB_NAME, ANALYSIS_DESIGN_DOC, "getStats")["rows"][0]["value"]


            for key in area_stats:
                emo_dict = area_stats[key]["emojis"]
                for emo_code in emo_dict:
                    emoji_count[emo_code] = emoji_count.get(emo_code,0) + emo_dict[emo_code]
            
            topFive = calculateTop(emoji_count, 5)

            data = []
            for each in topFive:
                data.append({
                    "emojicode": each[0],
                    "number": each[1]
                })

            return_json = {
                        "ok": True,
                        "data": data}
        except Exception as e:
            print(e)
            return_json = {
                "ok": False,
                "msg" : "Something went wrong: "}
        return return_json
        
api.add_resource(getTopFiveEmoji, '/getTopFiveEmoji', endpoint = 'getTopFiveEmoji')  

############### api: /topfiveemoji

# top five emoji of victoria , return a list of top 5 emoji codes in vic 
# {
#     "ok": True,
#     "data": [
#         "emojicode "
#     ] 


# }


if __name__ == '__main__':
    app.run( debug = True,host="0.0.0.0",port=5000)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello, World!"

# @app.route('/')


# if __name__ == '__main__':
#     app.run(debug=True,host="0.0.0.0",port=5000)




