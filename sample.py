import tweepy
from tweepy import OAuthHandler

consumer_key = 'DHjYxfSwthP3CDCsoi2NAD1LD'
consumer_secret = 'gXjx7X9gqpB6EHnFtY87zXqzoUa5ar4B5CjpGv11Jy96ocSCYW'

access_token = '39007772-kSOdoKYkUJAZISv5HZLSMvcYzhR54tC4DDPelf6FO'
access_secret = '3ZuxhuVRrpczjUA3wsnq45Yt9zgeRZ2U7wbYiKPVovDhl'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

#status = "HAHAHHA"
#api.update_status(status=status)
#data = api.search('Bruno Mars',['ENG'])
#print(data[0])
#print(api.search('Bruno Mars'))

#for status in tweepy.Cursor(api.home_timeline).items(10):
#   print(status.text)



market=['$AAPL']
data = dict()
contents = list()
print(api.rate_limit_status())
cursor = tweepy.Cursor(api.search,q=market[0], count=10, lang='en')
for item in cursor.items():
	contents.append(data.text)
	contents.append(favorite_count)
	data[data.id] = 
#for item in cursor.items():
#	print(item.text)
	#print(item)
	#data.append(item)

#print(len(data))


#print(data[0])
