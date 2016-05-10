# -*- coding: utf-8 -*-

#This code implements method 4 by comparing the frequencies of terms in a sample
#to frequencies in a historical corpus
import json
import string
import re

#The relative size of the historical corpus and sample dataset
countData = 10
countSample = 2
tweets_data_path = '../Project/Data/tweetStream100k'

data = {}
counter = 0

#This file includes stop words, Twitter-related words, and inappropriate words
scratchText = open('scratchWords.txt').read()	

#10 repeated modules to add all the words to the historical dataset

#An older version of this code was far more modular and used a for loop, but it
#unfortunately broke down and kept throwing Indentation and Syntax errors
tweets_file1 = open(tweets_data_path+'01.txt', "r")

for line in tweets_file1:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 1'

tweets_file1.close()

tweets_file2 = open(tweets_data_path+'02.txt', "r")

for line in tweets_file2:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 2'

tweets_file2.close()

tweets_file3 = open(tweets_data_path+'03.txt', "r")

for line in tweets_file3:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 3'

tweets_file3.close()

tweets_file4 = open(tweets_data_path+'04.txt', "r")

for line in tweets_file4:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 4'

tweets_file4.close()

tweets_file5 = open(tweets_data_path+'05.txt', "r")

for line in tweets_file5:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 5'

tweets_file5.close()

tweets_file6 = open(tweets_data_path+'06.txt', "r")

for line in tweets_file6:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 6'

tweets_file6.close()

tweets_file7 = open(tweets_data_path+'07.txt', "r")

for line in tweets_file7:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 7'

tweets_file7.close()

tweets_file8 = open(tweets_data_path+'08.txt', "r")

for line in tweets_file8:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 8'

tweets_file8.close()

tweets_file9 = open(tweets_data_path+'09.txt', "r")

for line in tweets_file9:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 9'

tweets_file9.close()

tweets_file10 = open(tweets_data_path+'10.txt', "r")

for line in tweets_file10:
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
				data[parsed] += 1
			else:
				data[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 10'

tweets_file10.close()

print 'There are', counter/2, 'tweets in the background corpus'

#Code to store the term frequencies from the sample dataset

sample = {}
counter = 0

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

#Code to calculate the scores of each of the terms
for word in sample:
	#Ignore terms in the sample that occur fewer than 500 times - they're unlikely to be trending
	if sample[word] < 500:
		sample[word] = 0
	else:
		if word in data:
			dataSize = countSample*data[word]/countData + 1
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