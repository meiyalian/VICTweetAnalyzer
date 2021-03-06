import couchdb  # importing couchdb



host = "172.26.133.228"
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


def send_to_db(tweet, tid,  db = vic_tweets):
    try:
        if (tid not in db):
            db[tid] = tweet
            print("save!!")
            return True
    except:
        print("connection problem: " + str(tid))

    else:
        print("already in db")
        return False

