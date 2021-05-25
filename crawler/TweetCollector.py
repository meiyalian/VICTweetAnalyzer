# from flask import Flask 
import tweepy
import json
import csv
import argparse
import time
import argparse
from DBconnect import vic_tweets, send_to_db
from AurinAnalyzer import *
from TimeConverter import convert_to_local_time
import time
from queue import Queue
from threading import Thread
import logging
# the regular imports, as well as this:
from urllib3.exceptions import ProtocolError
from datetime import datetime
# from http.client import IncompleteRead 





#app key & secret 
consumer_key = '0BQfUFuL2P16vfMdoKWQe5cuk'
consumer_secret = 'XYEo4GhttDNIuy7dnvTJ9lEIyZqMoUZ6OaOeIMYMpavOG9u1EI'
access_token = '1387291113304727557-yyNyEBhdateaDTTQ5ck1Cyx0RrhABB'
access_token_secret = 'nTIJfKaT1XWsOHgONuOIZE9nhQUCL5TVa51eNs7amy0eS'

access = {"consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
            "access_token": access_token,
            "access_secret": access_token_secret}

VIC_bounding_box = [141.03,-38.41,148.7,-33.98]
VIC_geo = "-37.03521,145.23218,400km"



def initialization(): 
    print("Initializing ....... ")
    areas_polygons = {}
    area_lst = vic_tweets.view('vic_tweets/getAllAreaRanges')
    for each in area_lst:
        polys = convert_to_multipolygon(each.value)
        areas_polygons[each.id] = polys
    print(".......Initialization completed")
    return areas_polygons

   


area_polygons = initialization()


# Get the authentication
def getAuth(access):
    auth = tweepy.OAuthHandler(access['consumer_key'], access['consumer_secret'])
    auth.set_access_token(access['access_token'], access['access_secret'])
    return auth





def save_a_tweet(status, is_polygon,  area_dict , db = vic_tweets ):
    if (str(status.id) not in db):
        area = "Out Of Bound"
        if is_polygon:
            area = determine_location(area_dict,status.place.bounding_box.coordinates[0], isBoundingBox = True ) 
        else:
            area = determine_location(area_dict,status.coordinates["coordinates"], isBoundingBox = False ) 
        
        if area != "Out Of Bound":
            print("area is: " + area)
            try:
                if status.truncated == True:
                    tweet = status.extended_tweet['full_text'].lower()
                else:
                    tweet = status.text.lower()
            except:
                tweet = status.full_text.lower()
                
            #tweet document 
            tweet = {
                "type": "tweet",
                "text": tweet,
                "hashtags": status.entities['hashtags'],
                "time": convert_to_local_time(status.created_at),
                "location": area,
                "ts": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }

            send_to_db(tweet, str(status.id))
        else:
            print("area out of bound")


def process_status(status):
    if not hasattr(status, "retweeted_status")and status.lang=="en" and (status.coordinates is not None or status.place is not None) :  # if its not Retweet and is in English
        if status.coordinates is not None:
            save_a_tweet(status,  False, area_polygons)
        else:
             save_a_tweet(status, True, area_polygons)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, q = Queue()):
        super().__init__()
        # super(MyStreamListener, self).__init__()
        self.q = q
        num_worker_threads = 4
        for i in range(num_worker_threads):
            t = Thread(target=self.do_stuff)
            
            t.daemon = True
            t.start()
            
    def do_stuff(self):
        while True:
            try:
                item = self.q.get()
                if item is None:
                    continue
                #try:
     
                process_status(item)

                #finally:
                #    self.q.task_done()

            except queue.Empty:
                pass
            except:
                logging.exception('error while processing item')
      


    def on_status(self, status): 
        self.q.put(status)
    
       
    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_data disconnects the stream
            return False
    def on_limit(self, status):
        print ('Limit threshold exceeded', status)

    def on_timeout(self, status):
        print ('Stream disconnected; continuing...')





if __name__ == "__main__":  
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--stream",  help="streaming twitter" , action = 'store_true')
    parser.add_argument("--location",  help="streaming twitter --> specify (x1, y1, x2, y2), default set to Victoria" , nargs=4 , metavar=('x1', 'y1', 'x2', 'y2'), default = VIC_bounding_box)
    parser.add_argument("--search",  help="search twitter" ,action = 'store_true')
    parser.add_argument("--storeAurinData",  help="store data from Aurin" ,action = 'store_true')
    parser.add_argument("--area",  help="search twitter --> specify search area using string or default set to Victoria) " , default =VIC_geo)
    args = parser.parse_args()

    if args.storeAurinData:
        analyzer = AurinAnalyzer()
        analyzer.store_in_db()

    if args.stream:
        print("Start streaming ....... ")
        while True:
            try:
                locations = [float(args.location[0]),float(args.location[1]),float(args.location[2]),float(args.location[3])]
                myStreamListener = MyStreamListener()
                myStream = tweepy.Stream(auth = getAuth(access), listener=myStreamListener)
                myStream.filter(locations=locations, stall_warnings=True) #filter tweets from vic using https://boundingbox.klokantech.com/
            except KeyboardInterrupt: 
                myStream.disconnect()
                print('End Session.')
                break
            except ProtocolError:
                print("Something went wrong ... reconnecting")
                continue
            except Exception as e:
                pass 
            

        
    elif args.search:
        print("Start searching ....... ")

        api = tweepy.API(getAuth(access), wait_on_rate_limit=True)
        recent = api.search(geocode=VIC_geo, count=1, result_type='recent')


        max_id = recent[0].id+1

        collected = 0
        count = 0
        while True:
            try:
                new_search = api.search(q='*', count=300, lang="en", geocode=VIC_geo, tweet_mode="extended", max_id=str(max_id-1))
                # for status in tweepy.Cursor(api.search, q='*', lang="en",geocode=VIC_geo,tweet_mode="extended", max_id=max_id).items(300):
                for status in new_search:
                    if not hasattr(status, "retweeted_status") and (status.coordinates is not None or status.place is not None): 
                        count +=1
                        
                        if status.coordinates is not None:
                            save_a_tweet(status,  False, area_polygons)
                        else:
                            save_a_tweet(status,  True, area_polygons)
                        

                    max_id = status.id
            except KeyboardInterrupt: 
                print('End Session.')
                break

            except Exception as e:
                
                time.sleep(10)
                pass

    
 




# class TweetProcesser


# app = Flask(__name__)

# @app.route('/')
# def hellp_world():
#     return 'hello'


# app.run(host='0.0.0.0', port=5000)