plt.show()

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

for piece in text.split():
    	if piece in wordList:
    		wordList[piece] += 1
    	else:
    		wordList[piece] = 1


import json
import pandas as pd
import matplotlib.pyplot as plt
import collections
import string

#def strip_punctuation(s):
 #   return ''.join(c for c in s if c not in string.punctuation)

tweets_data_path = 'tweetStream.txt'

hashtagList = {}
wordList = {}
counter = 0
tweets_file = open(tweets_data_path, "r")	
for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
	for hashtag in tweet['entities']['hashtags']:
		if hashtag in hashtagList:
			hashtagList[hashtag] += 1
		else:
			hashtagList[hashtag] = 1
	text = tweet['text'].split()
	#nopuncText = strip_punctuation(s)
	#text.translate(text.maketrans("",""), string.punctuation)
	#nopuncTextSplit = nopuncText.split()
	for word in text:
		print 'hi'
		print word
		print strip_punctuation(word)
	counter += 1
    except:
    	counter += 1
        continue

print 'There are', counter, 'tweets'

print hashtagList
print wordList
