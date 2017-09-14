import tweepy
import datetime
from tweepy import OAuthHandler

consumer_key = 'DHjYxfSwthP3CDCsoi2NAD1LD'
consumer_secret = 'gXjx7X9gqpB6EHnFtY87zXqzoUa5ar4B5CjpGv11Jy96ocSCYW'

access_token = '39007772-kSOdoKYkUJAZISv5HZLSMvcYzhR54tC4DDPelf6FO'
access_secret = '3ZuxhuVRrpczjUA3wsnq45Yt9zgeRZ2U7wbYiKPVovDhl'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
#api = tweepy.API(auth,wait_on_rate_limit = True)
api = tweepy.API(auth)
market=['$AAPL','$TXT','$GOOGL','$STZ','$GRMN','$CUTERA','$ULTA','$FEYE','$DLX','$T','$DISCA','$ABT','$BDX','$CVS','$XOM','$JNJ','$LOW','$MSFT','$SFM','$UTX']







while True:
	try:
		for i in range(0,len(market)):
			cursor = tweepy.Cursor(api.search, q=market[i], count=100, lang='en')
			filename = datetime.datetime.now().ctime() + market[i] + ".txt"
			name = 'DataSets/' + filename
			fileWriter = open(name,"w")
			for item in cursor.items():
				fileWriter.write(str(item))
				fileWriter.write("\n")
			fileWriter.close()	
	except tweepy.error.TweepError as e:
		print("Exceeded")
		


#for item in cursor.items():
#	print(item.text)
	#print(item)
	#data.append(item)

#print(len(data))


#print(data[0])
