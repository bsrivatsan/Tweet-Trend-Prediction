import json
import pandas as pd
import matplotlib.pyplot as plt
import collections

tweets_data_path = 'tweetStream.txt'

tweets_data = []
hashtagList = []
tweets_file = open(tweets_data_path, "r")	
for line in tweets_file:
    try:
        tweet = json.loads(line.strip())
        tweets_data.append(tweet)
	for hashtag in tweet['entities']['hashtags']:
		hashtagList.append(hashtag['text'])
    except:
        continue

print 'There are', len(tweets_data), 'tweets'

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet.get('text',None), tweets_data)
tweets['country'] = map(lambda tweet: tweet.get('place', {}).get('country') if tweet.get('place', None) != None else None, tweets_data)

print collections.Counter(hashtagList)

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

plt.show()