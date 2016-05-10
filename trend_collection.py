#This code is used to collect trends so that we can evaluate the success
#of each of our prediction methods

import tweepy
import time
import json

#Initialize the authentication with Tweepy's API wrapper
oauth = tweepy.OAuthHandler("0h7jv4PcQC5OImXLGNivhmpPp", "qQEVbSDX3WSfxfSXxItXTdX5nZLrrE0YINNrLrTbQEekencQTY")
oauth.set_access_token("701559036215431168-2Ln53aAlMZZUFL74hK3BlOCW2f7vEaO", "iUTgwVXYHcZwf3nq0Bpu98qpIQWMzLuQiScgWvpf19hFK")
api = tweepy.API(oauth)

trendsJson = open('../Project/Data/trendsJSON.txt',"a")
newTrends = []
counter = 0
#Collect trends for 2 hours at 10 minute intervals 
while counter < 12:
	currentTrends = api.trends_place(1)
	try:
		for trend in currentTrends['trends']:
			#Only add new trends to the list
 			if name not in newTrends:
				newTrends.append(name)
	except:
		continue
	counter += 1
	trendsJson.write(currentTrends)
	time.sleep(600)

trendDoc = open('Data/trends.txt',"w")
json.dump(newTrends, trendDoc)
trendDoc.close()
trendsJson.close()

print 'There are', len(newTrends), 'new trends'