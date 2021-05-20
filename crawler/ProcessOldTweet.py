
import csv
from DBconnect import vic_areas_tweets_db, send_to_db
from TimeConverter import convert_to_local_time

def processTweets(fpath, location):
    with open(fpath) as f:
        line_count = 0
        number_added = 0 
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if line_count >0:
                if (row[11] == "en"): # only english 
                    tweet_obj = {
                        "text": row[10],
                        "hashtags": eval(row[18]),
                        "time": convert_to_local_time(row[2].replace(" AEST", ""), True),
                        "location": location
                        }

                 
                    succeed = send_to_db(tweet_obj, str(row[0]))
                    if succeed:
                        number_added +=1 
            line_count +=1
    print("process " + str(number_added) + " tweets!")

    

processTweets("./tweetsCollect/tweets.csv", "Melbourne (C)")
