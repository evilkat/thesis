import json
import dbconnect
import tweepy
import datetime
from tweepy import OAuthHandler

def start_search(searchquery):

	consumer_key = 'DHjYxfSwthP3CDCsoi2NAD1LD'
	consumer_secret = 'gXjx7X9gqpB6EHnFtY87zXqzoUa5ar4B5CjpGv11Jy96ocSCYW'

	access_token = '39007772-kSOdoKYkUJAZISv5HZLSMvcYzhR54tC4DDPelf6FO'
	access_secret = '3ZuxhuVRrpczjUA3wsnq45Yt9zgeRZ2U7wbYiKPVovDhl'

	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_secret)
	api = tweepy.API(auth,wait_on_rate_limit = True)
	#api = tweepy.API(auth)
	#market=['$AAPL','$GOOGL','$MSFT']
	max_tweets = 1000
	print(api.rate_limit_status()['resources']['search'])
	tweetcount = 0
	while True:
		try:
			for tweet in tweepy.Cursor(api.search,q=searchquery,count=1000).items(max_tweets):
				dbconnect.connect(json.dumps(tweet._json))
		except tweepy.error.TweepError as e:
			print("Exceeded Limit")
	'''
	while True:
		try:
			#searched_tweets = [status._json for status in tweepy.Cursor(api.search,  q=searchquery).items(max_tweets)]
			#json_strings = [json.dumps(json_obj) for json_obj in searched_tweets]
			#for i in range(0,len(market)):
			for tweet in tweepy.Cursor(api.search,q=searchquery,count=1000).items(max_tweets):
				json_str = json.dumps(tweet._json)
			#print(type(json_strings))
			#print(json_strings)
					#stats = json.dumps(tweet)
					#print(type(stats))
					#print("hello")
					#print(tweet)
					#json_tweet = json.loads(tweet)
				dbconnect.connect(json_str)
		except tweepy.error.TweepError as e:
			print("Exceeded")
	'''
def main():
	query = '$AAPL or Apple or #Apple or #MAC or #MACOS or #Iphone'
	start_search(query)

main()
