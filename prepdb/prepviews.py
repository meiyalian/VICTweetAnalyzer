import couchdb  # importing couchdb
import pycouchdb
import json

"""
Run this script once to prepare the views document for couchdb


"""

host = "172.26.132.110"
port = "5984"
username = password = "admin"


def connect_to_couch_db_server(host, port, username, password):
    return pycouchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)


def connect_to_database(database_name, server):
    try:
        return server.database(database_name)
    except:
        return server.create(database_name)

if __name__ == "__main__":  

    dbserver = connect_to_couch_db_server(host, port, username, password)
    vic_tweets = connect_to_database("vic_tweets", dbserver)


    #prepare view for area 
    with open('prepdb/map_views.json', 'r') as f:
        vic_tweets.save(json.load(f))
