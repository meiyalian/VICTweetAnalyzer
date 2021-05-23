from datetime import datetime

from DBconnect import vic_tweets, send_to_db
from Areas import areas

from datetime import datetime


# def is_time_between(begin_time, end_time, check_time):
#     # If check time is not given, default to current UTC time
#     check_time = check_time 
#     if begin_time < end_time:
#         return check_time >= begin_time and check_time <= end_time
#     else: # crosses midnight
#         return check_time >= begin_time or check_time <= end_time



# # count = 0
# # for item in vic_tweets.view('_all_docs'):
# #     did = item.id
# #     doc = vic_tweets[did]
# #     if doc['type'] == "tweet":
# #         ts = doc['ts']
# #         convertts = datetime.strptime(ts, '%d/%m/%Y %H:%M:%S')
# #         print(convertts)
# #         if is_time_between(datetime(2021,5,22,8,40), datetime(2021,5,22,9,27),convertts ):
# #             vic_tweets.delete(did)
# #             print("delete 1 ")
# #             count +=1 
 
# # print("delete  " + str(count))

count = 0
for item in vic_tweets.view('vic_tweets/getFaulty'):
    id = item.key
    print(id)
    doc = vic_tweets[id]
    vic_tweets.delete(doc)
    count+=1
print("delete" + str(count))


# v =  vic_tweets.view('vic_tweets/getTweetAreaCount', group = True)
# print(v)
# for each in v:
#     if each.key in areas:
#         print(each.key, each.value)



# v =  vic_tweets.view('vic_tweets/getTweetAreaCount', group = True)
# print(v)
# for each in v:
#     if each.key in areas: 
#         print(each.key, each.value)


