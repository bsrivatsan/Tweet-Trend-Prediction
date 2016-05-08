# -*- coding: utf-8 -*-
import json
import string
import re

tweets_data_path = 'Data/tweetStream100k01'

hashtagList = {}
wordList = {}
counter = 0
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
			if parsed in wordList:
				wordList[parsed] += 1
			else:
				wordList[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'There are', counter/2, 'tweets'

words = open(tweets_data_path+'Words.txt',"w")
json.dump(sorted(wordList.items(), key=lambda x:x[1], reverse=True), words)
words.close()
print 'There are', len(wordList), 'words'

hashtags = open(tweets_data_path+'Hashtags.txt',"w")
json.dump(sorted(hashtagList.items(), key=lambda x:x[1], reverse=True), hashtags)
hashtags.close()
print 'There are', len(hashtagList), 'hashtags'