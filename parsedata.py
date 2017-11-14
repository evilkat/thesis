import sentiment
import pymongo
from pymongo import MongoClient
import re

def cleanData(count,timestamptweet,textvalue,rtc,fc,mention,irt):
    #pattern = re.compile('\w+')
    #msg = pattern.search(pattern,textvalue)
    msg=re.sub(r'[^\w]'," ",textvalue)
    #print(msg)
    count=sentiment.computeSentiment(count,timestamptweet,msg,rtc,fc,mention,irt)
    return count

def getData():
    client = pymongo.MongoClient("localhost",27017)
    db = client['twitterdata_clean']
    collection = db['twitterdata_clean']
    result = collection.find()
    count = 0
    for obj in collection.find():
        #print(obj['created_at'],obj['geo'])
        if 'created_at' in obj.keys():
            count=cleanData(count,obj['created_at'],obj['text'],obj['retweet_count'],obj['favorite_count'],len(obj['user_mentions']),obj['is_retweeted'])

    print(count)

getData()
