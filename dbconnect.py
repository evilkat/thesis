from pymongo import MongoClient
import pymongo
import json
import datetime
import time

def connect(datatweet):
    try:
        client = pymongo.MongoClient("localhost",27017)
        db = client['twitterdata2']
        collection = db['twitterdata2']

        #tweet = json.dumps((datatweet))
        collection.insert(json.loads(datatweet))
        #print(tweet)
        #print("Insert")
        return True
    except BaseException as e:
        print('Failed on Data ',str(e))
        time.sleep(5)
        pass
        exit()
