import sentiment
import pymongo
from pymongo import MongoClient
import re

def cleanData(count,timestamptweet,textvalue,rtc,fc,mention):
    #pattern = re.compile('\w+')
    #msg = pattern.search(pattern,textvalue)
    msg=re.sub(r'[^\w]'," ",textvalue)
    #print(msg)
    count=sentiment.computeSentiment(count,timestamptweet,msg,rtc,fc,mention)
    return count

def getData():
    client = pymongo.MongoClient("localhost",27017)
    db = client['twitterdata2']
    collection = db['twitterdata2']
    result = collection.find()
    count = 0
    for obj in collection.find():
        #print(obj['created_at'],obj['geo'])
        count=cleanData(count,obj['created_at'],obj['text'],obj['retweet_count'],obj['favorite_count'],len(obj['entities']['user_mentions']))

    print(count)

getData()
