# -*- coding: utf-8 -*-

#This code implements the last algorithm by tracking changes in word usage
#Uses http://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
import json
import string
import re

tweets_data_path = '../Project/Data/tweetStream100k'

wordList1 = {}
wordList2 = {}
wordList3 = {}
wordList4 = {}
wordList5 = {}

counter = 0
tweets_file1 = open(tweets_data_path+'06.txt', "r")

#This file includes stop words, Twitter-related words, and inappropriate words
scratchText = open('scratchWords.txt').read()	

#5 repeated code sections to add all of the frequency counts to the respective dictionaries

#Uses http://stackoverflow.com/questions/16129652/accessing-json-elements
for line in tweets_file1:
    try:
        tweet = json.loads(line.strip())
	#Code to store counts for all words
	text = tweet['text'].split()
	for word in text:
		#Parsing words to strip all punctuation and convert to lower case
		#From https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string
		parsed = ''.join(c for c in word if c not in string.punctuation)
		parsed = parsed.lower()
		if parsed not in scratchText:
			if parsed in wordList1:
				wordList1[parsed] += 1
			else:
				wordList1[parsed] = 1
   	counter += 1
    except:
    	counter += 1
        continue

print 'Completed File 1'

tweets_file1.close()

tweets_file2 = open(tweets_data_path+'07.txt', "r")

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
			if parsed in wordList2:
				wordList2[parsed] += 1
			else:
				wordList2[parsed] = 1
    except:
        continue

print 'Completed File 2'

tweets_file2.close()

tweets_file3 = open(tweets_data_path+'08.txt', "r")

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
			if parsed in wordList3:
				wordList3[parsed] += 1
			else:
				wordList3[parsed] = 1
    except:
        continue

print 'Completed File 3'

tweets_file3.close()

tweets_file4 = open(tweets_data_path+'09.txt', "r")

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
			if parsed in wordList4:
				wordList4[parsed] += 1
			else:
				wordList4[parsed] = 1
    except:
        continue

print 'Completed File 4'

tweets_file4.close()

tweets_file5 = open(tweets_data_path+'10.txt', "r")

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
			if parsed in wordList5:
				wordList5[parsed] += 1
			else:
				wordList5[parsed] = 1
    except:
        continue

print 'Completed File 5'

tweets_file5.close()

#Computes the score of each of the terms using our algorithm
growthSort = {}

for key in wordList5.keys():
	val5 = wordList5[key]
	if key in wordList4:
		val4 = wordList4[key]
	else:
		val4 = 0
	if key in wordList3:
		val3 = wordList3[key]
	else:
		val3 = 0		
	if key in wordList2:
		val2 = wordList2[key]
	else:
		val2 = 0
	if key in wordList1:
		val1 = wordList1[key]
	else:
		val1 = 0

	grow = 0.4 * (val5 - val4) + 0.3 * (val4 - val3) + 0.2 * (val3 - val2) + 0.1 * (val2 - val1)
	growthSort[key] = grow


print 'There are', counter/2, 'tweets'

#Storage into data
#Uses http://stackoverflow.com/questions/16772071/sort-dict-by-value-python
words = open(tweets_data_path+'GrowthWords.txt',"w")
json.dump(sorted(growthSort.items(), key=lambda x:x[1], reverse=True), words)
words.close()
print 'There are', len(growthSort), 'words'