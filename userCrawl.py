# -*- coding: utf-8 -*-
import tweepy
import string
import json

if __name__ == '__main__':

	scratchText = open('scratchWords.txt').read()	

	auth = tweepy.OAuthHandler("0h7jv4PcQC5OImXLGNivhmpPp", "qQEVbSDX3WSfxfSXxItXTdX5nZLrrE0YINNrLrTbQEekencQTY")
	auth.set_access_token("701559036215431168-2Ln53aAlMZZUFL74hK3BlOCW2f7vEaO", "iUTgwVXYHcZwf3nq0Bpu98qpIQWMzLuQiScgWvpf19hFK")
	api = tweepy.API(auth)

	user = 'b_srivatsan'
	wordList = {}

	#statuses = api.user_timeline(user)
	statuses = api.home_timeline()
	for status in statuses:	
		text = status.text.split()
		for word in text:
			parsed = ''.join(c for c in word if c not in string.punctuation)
			parsed = parsed.lower()	
			if parsed not in scratchText:
				if parsed in wordList:
					wordList[parsed] += 1
				else:
					wordList[parsed] = 1

	userTweets = open('Data/userTweets.txt',"w")
	json.dump(sorted(wordList.items(), key=lambda x:x[1], reverse=True), userTweets)
	userTweets.close()
	print 'There are', len(wordList), 'words'