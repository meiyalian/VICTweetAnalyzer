# import GetOldTweets3 as got 
import argparse
from TweetCollector import initialization
from DBconnect import vic_tweets, send_to_db
from TimeConverter import convert_to_local_time
from Areas import areas
import twint
import os
from ProcessOldTweet import processTweets
import requests
parser = argparse.ArgumentParser()
# parser.add_argument('--geo', type=str, default="-37.80811,144.96071,50mi")
parser.add_argument('--startdate', type=str, default="2019-12-01")
parser.add_argument('--enddate', type=str, default="2021-5-20")
parser.add_argument('--limit', type=int, default=50000)
args = parser.parse_args()

for key in areas:
    geo_string = str(areas[key]["lat"]) + "," + str(areas[key]["lng"]) + "," + "15km"
    c = twint.Config()
    
    c.Proxy_host = "127.0.0.1"
    c.Proxy_port = "9324"
    c.Proxy_type = "http"
    c.Since= args.startdate
    c.Until = args.enddate
    c.Limit = args.limit
    c.Lang = "en"
    c.Filter_retweets = True
    c.Geo = geo_string
    c.Store_csv = True
    c.Output = "Collected"
    try:
        twint.run.Search(c)
    except: 
        twint.run.Search(c)

    
    print("Start processing collected tweets ..... ")
    
    processTweets("Collected/tweets.csv", key)
    print("......Finish processing")
    try:
        os.remove("Collected/tweets.csv")
        print("Collected data Uploaded to DB --> Local File Removed!")
    except: 
        pass