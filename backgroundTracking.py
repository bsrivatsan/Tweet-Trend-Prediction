# -*- coding: utf-8 -*-

import json
import string
import re

countData = 10
countSample = 2
tweets_data_path = '../Project/Data/tweetStream100k'

data = {}

scratchText = open('scratchWords.txt').read()	

i = 1
while i <= countData:
	if i < 10:
		day = open(tweets_data_path+'0'+str(i)+'.txt',"r")
	else:
		day = open(tweets_data_path+str(i)+'.txt',"r")
	for line in day:
		try:
			tweet = json.loads(line.strip())
			#Code to store counts for all words
		text = tweet['text'].split()
		for word in text:
			#Parsing words to strip all punctuation and convert to lower case
			parsed = ''.join(c for c in word if c not in string.punctuation)
			parsed = parsed.lower()
			if parsed not in scratchText:
				if parsed in data:
					data[word] += 1
				else:
					data[word] = 1
		counter += 1
	    except:
	    	counter += 1
	        continue
	day.close()
	print 'Completed set', i
	i+=1

sample = {}

testData = open('../Project/Data/tweetStream200kSample.txt',"r")
for line in testData:
    try:
        tweet = json.loads(line.strip())
	#Code to store counts for all words
	text = tweet['text'].split()
	for word in text:
		#Parsing words to strip all punctuation and convert to lower case
		parsed = ''.join(c for c in word if c not in string.punctuation)
		parsed = parsed.lower()
		if parsed not in scratchText:
			if parsed in sample:
				sample[parsed] += 1
			else:
				sample[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'There are', counter/2, 'tweets'
testData.close()

for word in sample:
	if sample[word] < 500:
		sample[word] = 0
	else:
		if word in data:
			dataSize = countSample*data[word]/countData
			#Divide by dataSize so as to not drastically prioritize large values
			diff = (sample[word] - dataSize)/dataSize
			#Cubed so that we still maintain positive/negative differences
			#Negative difference words cannot be trending
			sample[word] = diff*diff*diff
		else:
			diff = (sample[word] - 50)/50
			sample[word] = (diff*diff*diff)

backgroundTrack = open(tweets_data_path+'backgroundTrack.txt',"w")
json.dump(sorted(sample.items(), key=lambda x:x[1], reverse=True), backgroundTrack)
backgroundTrack.close()
print 'There are', len(data), 'words'