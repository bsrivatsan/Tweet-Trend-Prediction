# -*- coding: utf-8 -*-

#This code performs the method 3 algorithm by weighting the terms used in authority figure tweets
import json
import string
import re
import numpy
import matplotlib.pyplot as plt

tweets_data_path = '../Project/Data/tweetStream200kSample'

#Maintain data structures to keep track of words and counts/booleans
wordList = {}
authorityList = {}
hashtagList = {}
verifiedList = {}

tweetCounter = 0

tweets_file = open(tweets_data_path+'.txt', "r")

#This file includes stop words, Twitter-related words, and inappropriate words
scratchText = open('scratchWords.txt').read()	
for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
    #Compile the hashtag list
	for hashtag in tweet['entities']['hashtags']:
		tag = hashtag['text']
		if tag not in scratchText:
			if tag in hashtagList:
				hashtagList[tag] += 1
			else:
				hashtagList[tag] = 1
	text = tweet['text'].split()
	for word in text:
		#Parse each word by stripping punctuation and lower-casing
		parsed = ''.join(c for c in word if c not in string.punctuation)
		parsed = parsed.lower()
		if parsed not in scratchText:
			#Update the max followers, verified tweets, and number of use counts for each word
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

print 'There are', tweetCounter/2, 'tweets'


#Plotting the histograms for the values in the three distributions
n, bins, patches = plt.hist(wordList.values(), bins=numpy.arange(min(wordList.values()), max(wordList.values()) + 10, 10))
plt.xlabel('Numbers of Tweets per Word')
plt.ylabel('Frequency of Words')
plt.title('Histogram of Word Frequencies')
plt.axis([0, 200, 0,100000])
plt.show()

n, bins, patches = plt.hist(verifiedList.values(), bins=numpy.arange(min(verifiedList.values()), max(verifiedList.values()) + 1, 1))
plt.xlabel('Numbers of Verified Users per Word')
plt.ylabel('Frequency of Words')
plt.title('Histogram of Verified User Frequencies')
plt.axis([0, 5, 0,100000])
plt.show()

n, bins, patches = plt.hist(authorityList.values(), bins=numpy.arange(min(authorityList.values()), max(authorityList.values()) + 25000, 25000))
plt.xlabel('Max Followers per Word')
plt.ylabel('Frequency of Words')
plt.title('Histogram of Max Follower Frequencies')
plt.axis([0, 0.3e6, 0,100000])
plt.show()


#Taking the log for all of the three distributions
#Add 1 to each value so we never take log(0)
for key,value in wordList.items():
	wordList[key]=numpy.log(numpy.log(value + 1) + 1)
for key,value in verifiedList.items():
	verifiedList[key]=numpy.log(value + 1)
for key,value in authorityList.items():
	authorityList[key]=numpy.log(value + 1)

#Plot the new, re-scaled versions
n, bins, patches = plt.hist(wordList.values(), )
plt.xlabel('Numbers of Tweets per Word')
plt.ylabel('Frequency of Words')
plt.title('Histogram of Log Log Word Frequencies')
#plt.axis([0, 1000, 0,200,000])
plt.show()

n, bins, patches = plt.hist(verifiedList.values())
plt.xlabel('Numbers of Verified Users per Word')
plt.ylabel('Frequency of Words')
plt.title('Histogram of Log Verified User Frequencies')
#plt.axis([0, 10, 0,200,000])
plt.show()

n, bins, patches = plt.hist(authorityList.values())
plt.xlabel('Max Followers per Word')
plt.ylabel('Frequency of Words')
plt.title('Histogram of Log Max Follower Frequencies')
#plt.axis([0, 0.4e7, 0,200,000])
plt.show()


#Calculate the z-scores for each of these metrics
wordMean = numpy.mean(wordList.values())
wordStd = numpy.std(wordList.values())
for key,value in wordList.items():
    z=(value-wordMean)/wordStd 
    wordList[key]=z

verMean = numpy.mean(verifiedList.values())
verStd = numpy.std(verifiedList.values())
for key,value in verifiedList.items():
    z=(value-verMean)/verStd 
    verifiedList[key]=z

authMean = numpy.mean(authorityList.values())
authStd = numpy.std(authorityList.values())
for key,value in authorityList.items():
    z=(value-authMean)/authStd 
    authorityList[key]=z

#Parameters to use in final equation
alpha = 1
beta = 1.5
gamma = 1.5
delta = 4

mixedList = {}

#Final equation to compute scores for each term
for key,value in wordList.items():
	score = alpha*value + beta*authorityList[key] + gamma*verifiedList[key]
	if key in hashtagList:
		score *= delta
	mixedList[key] = score

authorityWords = open(tweets_data_path+'AuthorityWords.txt',"w")
json.dump(sorted(mixedList.items(), key=lambda x:x[1], reverse=True), authorityWords)
authorityWords.close()