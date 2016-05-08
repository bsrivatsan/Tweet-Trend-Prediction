# -*- coding: utf-8 -*-
import json
import string
import re
import numpy

tweets_data_path = 'Data/tweetStream100k01'

wordList = {}
authorityList = {}
hashtagList = {}
verifiedList = {}

tweetCounter = 0

tweets_file = open(tweets_data_path+'.txt', "r")

scratchText = open('scratchWords.txt').read()	
for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
	for hashtag in tweet['entities']['hashtags']:
		tag = hashtag['text']
		if tag not in scratchText:
			if tag in hashtagList:
				hashtagList[tag] += 1
			else:
				hashtagList[tag] = 1
	text = tweet['text'].split()
	for word in text:
		parsed = ''.join(c for c in word if c not in string.punctuation)
		parsed = parsed.lower()
		if parsed not in scratchText:
			followers = tweet['user']['followers_count']
			verified = tweet['user']['verified']
			if parsed in wordList:
				wordList[parsed] += 1
				if authorityList[parsed] < followers:
					authorityList[parsed] = followers
				if verified:
					verifiedList[parsed] += 1
			else:
				wordList[parsed] = 1
				authorityList[parsed] = followers
				if verified:
					verifiedList[parsed] = 1
				else:
					verifiedList[parsed] = 0		
   	tweetCounter += 1
    except:
    	tweetCounter += 1
        continue

print 'There are', counter/2, 'tweets'

#Calculate the z-scores for each of these metrics
wordMean = numpy.mean(wordList.items())
wordStd = numpy.std(wordList.items())
for key,value in wordList.items():
    z=(value-wordMean)/wordStd 
    wordList[key]=z

verMean = numpy.mean(verifiedList.items())
verStd = numpy.std(verifiedList.items())
for key,value in verifiedList.items():
    z=(value-verMean)/verStd 
    verifiedList[key]=z

authMean = numpy.mean(authorityList.items())
authStd = numpy.std(authorityList.items())
for key,value in authorityList.items():
    z=(value-authMean)/authStd 
    authorityList[key]=z

mixedList = {}



authorityWords = open(tweets_data_path+'AuthorityWords.txt',"w")
json.dump(sorted(mixedList.items(), key=lambda x:x[1], reverse=True), authorityWords)
authorityWords.close()

print 'There are', len(wordList), 'words'

