import json
import requests

RAW_TWEET_DB_NAME = "vic_tweets"
RAW_TWEET_DESIGN_DOC = "vic_tweets"
HOST = "172.26.133.228"
PORT = "5984"
USER_NAME  = "admin"
PWD = "admin"
ANALYSIS_DB_NAME = "analysis" 
ANALYSIS_DESIGN_DOC = "analysis"

GET_VIEW_URL = "http://{username}:{password}@{host}:{port}/{database}/_design/{design_doc}/_view/{view_name}"
GET_VIEW_URL_WITH_GROUP = "http://{username}:{password}@{host}:{port}/{database}/_design/{design_doc}/_view/{view_name}?group=True"



def getStats(database, design_doc, view, user = USER_NAME, password = PWD, host = HOST , port= PORT,  group = False):
    """
        return a json object containing the view result 

    """

    if group:
        return json.loads(requests.get(GET_VIEW_URL_WITH_GROUP.format(username = user,password = password, host = host, port = port,database = database, design_doc = design_doc, view_name = view)).content.decode("utf-8"))
    else:
        return json.loads(requests.get(GET_VIEW_URL.format(username = user, password = password, host = host, port = port,database = database, design_doc = design_doc, view_name = view)).content.decode("utf-8"))




