# -*- coding: utf-8 -*-

#This code implements the recommendation system of our project
#Uses http://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
import tweepy
import string
import json

if __name__ == '__main__':

	scratchText = open('scratchWords.txt').read()	

	#Authenticates our requests to the Twitter ervers
	auth = tweepy.OAuthHandler("0h7jv4PcQC5OImXLGNivhmpPp", "qQEVbSDX3WSfxfSXxItXTdX5nZLrrE0YINNrLrTbQEekencQTY")
	auth.set_access_token("701559036215431168-2Ln53aAlMZZUFL74hK3BlOCW2f7vEaO", "iUTgwVXYHcZwf3nq0Bpu98qpIQWMzLuQiScgWvpf19hFK")
	api = tweepy.API(auth)

	#Sample case - search for recommendations for Bharath
	user = 'EdFelten'
	wordList = {}

	#Obtain statuses of user and friends
	statuses = api.user_timeline(user)
	for status in statuses:	
		text = status.text.split()
		for word in text:
			#From https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string
			parsed = ''.join(c for c in word if c not in string.punctuation)
			parsed = parsed.lower()	
			if parsed not in scratchText:
				if parsed in wordList:
					wordList[parsed] += 1
				else:
					wordList[parsed] = 1

	#Uses http://stackoverflow.com/questions/16772071/sort-dict-by-value-python
	userTweets = open('../Project/Data/' +user + 'Tweets.txt',"w")
	json.dump(sorted(wordList.items(), key=lambda x:x[1], reverse=True), userTweets)
	userTweets.close()
	print 'There are', len(wordList), 'words the user has tweeted'

	#Return recommendations
	count = 0
	highWords = open('../Project/Data/recommend.txt','r')
	words = highWords.readlines()
	for num, word in enumerate(words,1):
		if count > 5:
			break
		if word in wordList:
			print word
			count += 1

	highWords.close()