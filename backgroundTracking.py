import json

countData = 10
countSample = 2
tweets_data_path = 'Data/tweetStream100k'

data = {}

i = 1
while i <= countData:
	if i < 10:
		day = open(tweets_data_path+'0'+i+'.txt',"r")
	else:
		day = open(tweets_data_path+i+'.txt',"r")
	dayData = json.load(day)
	for word in dayData:
		if word in data:
			data[word] += dayData[word]
		else:
			data[word] = dayData[word]
	day.close()
	i+=1

testData = open('Data/tweetStreamSampleWords.txt',"r")
sample = json.load(testData)
testData.close()

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
			diff = sample[word] - 50
			sample[word] = (diff*diff*diff)/50

backgroundTrack = open(tweets_data_path+'backgroundTrack.txt',"w")
json.dump(sorted(sample.items(), key=lambda x:x[1], reverse=True), backgroundTrack)
backgroundTrack.close()
print 'There are', len(data), 'words'