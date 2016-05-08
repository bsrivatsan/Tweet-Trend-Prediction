import json

countData = 1
countSample = 1
tweets_data_path = 'Data/tweetStream100k'

data = {}

i = 1
while i <= countData:
	day = open(tweets_data_path+'0'+i+'.txt',"r")
	dayData = json.load(day)
	for word in dayData:
		if word in data:
			data[word] += dayData[word]
		else:
			data[word] = dayData[word]
	day.close()
	i+=1

sample = open('Data/tweetStream100kSample.txt',"r")
testData = json.load(sample)
sample.close()

for word in sample:
	if sample[word] < 500:
		sample[word] = 0
	else:
		if word in data:
			dataSize = countSample*data[word]/countData
			diff = sample[word] - dataSize
			#Cubed so that we still maintain positive/negative differences
			#Negative difference words cannot be trending
			sample[word] = (diff * diff * diff)/dataSize
		else:
			diff = sample[word] - 100
			sample[word] = (diff*diff*diff)/100

backgroundTrack = open(tweets_data_path+'backgroundTrack.txt',"w")
json.dump(sorted(data.items(), key=lambda x:x[1], reverse=True), backgroundTrack)
backgroundTrack.close()
print 'There are', len(data), 'words'