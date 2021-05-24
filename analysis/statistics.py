import re
import emoji
import numpy as np
import emoji, json
import time
import couchdb  # importing couchdb
from datetime import datetime

# from sentiment import vic_tweets, analysis #import db

host = "172.26.132.110"
port = "5984"
username = password = "admin"


def connect_to_couch_db_server(host, port, username, password):
    return couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)


def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)


dbserver = connect_to_couch_db_server(host, port, username, password)
vic_tweets = connect_to_database("vic_tweets", dbserver)
analysis = connect_to_database("analysis", dbserver)

while True:


    try:
        print("start updating ...")
        area_dict = {}

        hour_dict = {}
        positive_per_area =  analysis.view('analysis/getPositiveAmountByArea', group = True)
        negative_per_area = analysis.view('analysis/getNegativeAmountByArea', group = True)
        hour_pos = analysis.view('analysis/getTweetPosbyHour', group = True)
        hour_neg = analysis.view('analysis/getTweetNegbyHour', group = True)

        # positive_per
        emoji_counts = analysis.view('analysis/getEmoji')

        for each in positive_per_area:
            area_dict[each.key] = { "emojis": {}} 
            area_dict[each.key]["positive"] = each.value 
        
        for each in negative_per_area:
            area_dict[each.key]["negative"] = each.value 

        for each in hour_pos:
            hour_dict[each.key] = {"emojis": {}}
            hour_dict[each.key]["positive"] = each.value
        
        for each in hour_pos:
            hour_dict[each.key]["negative"] = each.value


        for each in emoji_counts:

            emoji = each.value["emoji"]
            hour = each.value["hour"]
            hour_dict[hour]["emojis"][emoji]  = hour_dict[hour]["emojis"].get(emoji, 0) + 1
            area_dict[each.key]["emojis"][emoji] = area_dict[each.key]["emojis"].get(emoji, 0) + 1


       
        area_stas = {
            "type": "statistics",
            "ts": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "areas": area_dict
        }


        hour_stas = {
            "type": "statistics",
            "ts": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "hours": hour_dict
        }
        print(hour_dict)
        try:
            doc = analysis.get("area_stas")
            hour_doc = analysis.get("hour_stas")
            if doc is None:
                analysis["area_stas"] = area_stas
            else:
       
                doc["ts"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                doc["areas"] = area_dict
                analysis.save(doc)
     
            if hour_doc is None:
                analysis["hour_doc"] = hour_stas
            else:
                hour_doc["ts"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                hour_doc["hours"] = hour_dict
                analysis.save(hour_doc)

        except Exception as e:
            print(e)
           
  
        print("... update completed ")
# count = 0
# for each in v:
#     count +=1 
# print(count)


        time.sleep(1000)
    except KeyboardInterrupt:
        print("End session.")
        break

    except Exception as e:
        print(e)









