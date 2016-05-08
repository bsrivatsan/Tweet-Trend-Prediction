import tweepy
import time
import json

oauth = tweepy.OAuthHandler("0h7jv4PcQC5OImXLGNivhmpPp", "qQEVbSDX3WSfxfSXxItXTdX5nZLrrE0YINNrLrTbQEekencQTY")
oauth.set_access_token("701559036215431168-2Ln53aAlMZZUFL74hK3BlOCW2f7vEaO", "iUTgwVXYHcZwf3nq0Bpu98qpIQWMzLuQiScgWvpf19hFK")
api = tweepy.API(auth = oauth)

newTrends = []
counter = 0
while counter < 12:
	currentTrends = api.trends_place(1)
	for line in currentTrends:
		try:
			trend = json.loads(line.strip())
			if trend['text'] not in newTrends:
				newTrends.append(trend['text'])
		except:
			continue
	counter += 1
	time.sleep(600)

trendDoc = open('Data/trends.txt',"w")
json.dump(newTrends, trendDoc)
trendDoc.close()

print 'There are', len(newTrends), 'new trends'