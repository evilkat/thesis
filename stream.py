from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import dbconnect

consumer_key = 'DHjYxfSwthP3CDCsoi2NAD1LD'
consumer_secret = 'gXjx7X9gqpB6EHnFtY87zXqzoUa5ar4B5CjpGv11Jy96ocSCYW'

access_token = '39007772-kSOdoKYkUJAZISv5HZLSMvcYzhR54tC4DDPelf6FO'
access_secret = '3ZuxhuVRrpczjUA3wsnq45Yt9zgeRZ2U7wbYiKPVovDhl'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
#api = tweepy.API(auth,wait_on_rate_limit = True)

class StdOutListener(StreamListener):
    def on_data(self,data):
        #print(data)
        print(type(data))
        #tweet = json.loads(data)
        dbconnect.connect(data)
        #dbconnect.connect(json.dumps(tweet._json))
        return True

    def on_error(self,status):
        print(status)

l = StdOutListener()
stream = Stream(auth,l)
stream.filter(track=['$AAPL','Apple or $AAPL','MACOS','Iphone'])
