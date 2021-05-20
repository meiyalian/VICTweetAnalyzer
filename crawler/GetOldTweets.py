# import GetOldTweets3 as got
import argparse
from TweetCollector import initialization
from DBconnect import vic_areas_tweets_db, send_to_db
from TimeConverter import convert_to_local_time
import twint

# import mpi4py
# from mpi4py import MPI

parser = argparse.ArgumentParser(description='COMP90024 Project Twitter Get By Geolocation')
parser.add_argument('--coordinates', type=str, default="-37.03521,145.23218")
parser.add_argument('--startdate', type=str, default="2021-01-01")
parser.add_argument('--enddate', type=str, default="2021-4-30")
parser.add_argument('--within', type=str, default="400km")
parser.add_argument('--max', type=int, default=1)
args = parser.parse_args()

c = twint.Config()
c.Store_object = True
c.Since="2021-01-01"
c.Until = "2021-04-30"
c.Limit = 10000
c.Lang = "en"
c.Filter_retweets = True

c.Geo = "-37.80811,144.96071,50mi"
c.Store_csv = True
c.Output = "tweetsCollect"
twint.run.Search(c)

tlist = []
c.Store_object_tweets_list = tlist
print(tlist)

# # tweetCriteria = got.manager.TweetCriteria().setNear(args.coordinates).setWithin(args.within)\
#                                            .setSince(args.startdate)\
#                                            .setUntil(args.enddate)\
#                                            .setMaxTweets(args.max)

# tweetlist = got.manager.TweetManager.getTweets(tweetCriteria)

# area_dicts = initialization()
# for tweet in tweetlist:
#         # tweet.text = tweet.text.lower()
# 		# if not tweet.text.startswith('rt'): #filter retweet 

#         #     tweet, tid = process_old_tweet(tweet)
#             # send_to_db(tweet,tid)
#         print(process_old_tweet(tweet))



def process_old_tweet(tweet):
    tweet_obj = {
        "text": tweet.text,
        "hashtags": tweet.hashtags,
        "time": convert_to_local_time(tweet.date, True),
        "location": tweet.geo
    }
    return tweet_obj, str(tweet.id)


