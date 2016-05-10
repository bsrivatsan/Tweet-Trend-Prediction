# -*- coding: utf-8 -*-

#This code uses the Tweepy Streaming API to collect tweets
#Uses http://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
import tweepy

#Number of tweets to collect
numTweets = 200000

#Basic listener that prints tweets to stdout, piped by user into data file
#Based on http://adilmoujahid.com/posts/2014/07/twitter-analytics/, https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/
class StdOutListener(tweepy.StreamListener):

    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0

    #Based on http://stackoverflow.com/questions/20863486/tweepy-streaming-stop-collecting-tweets-at-x-amount
    def on_data(self, data):
        print data
        self.num_tweets += 1
        if self.num_tweets < numTweets:
            return True
        else:
            #print 'Exceeded cap of', numTweets
            return False

    def on_error(self, status):
        print 'Error on status', status

    def on_limit(self, status):
        print 'Limit threshold exceeded', status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener = StdOutListener()
    oauth = tweepy.OAuthHandler("0h7jv4PcQC5OImXLGNivhmpPp", "qQEVbSDX3WSfxfSXxItXTdX5nZLrrE0YINNrLrTbQEekencQTY")
    oauth.set_access_token("701559036215431168-2Ln53aAlMZZUFL74hK3BlOCW2f7vEaO", "iUTgwVXYHcZwf3nq0Bpu98qpIQWMzLuQiScgWvpf19hFK")
    stream = tweepy.Stream(auth = oauth, listener=listener)

    #This line filters the stream to only include english tweets with #s
    stream.filter(track=['#', 'the','i','to','a','and','is','in','it','you','of','tinyurl.com','for','on','my','s','that','at','with','me','do','have','just','this','be','nt','so','are','m','not','was','but','out','up','what','now','new','from','your','like','good','no','get','all','about','we','if','time','as','day','will','one','twitter','how','can','some','an','am','by','going','they','go','or','has','rt','know','today','there','love','more','work','=','too','got','he','back','think','did','lol','when','see','really','had','great','off','would','need','here','thanks','been','blog','still','people','who','night','ll','want','why','bit.ly','home','re','should','well','oh','much','u','ve','then','right','make','last','over','way','cant','does','getting','watching','its','only','her','post','his','morning','very','she','them','could','first','than','better','after','tonight','our','again','down','twitpic.com','news','man','im','looking','us','tomorrow','best','into','any','hope','week','nice','show','yes','where','take','check','come','trying','fun','say','working','next','happy','were','even','live','watch','feel','thing','life','little','never','something','bad','free','doing','world','ff.im','video','sure','yeah','bed','let','use','their','look','being','long','done','sleep','before','year','find','awesome','big','un','+','things','ok','another','d','him','cool','old','ever','help','anyone','made','ready','days','die','other','read','because','two','playing','though','is.gd','house','always','also','listening','maybe','please','wow','haha','having','thank','pretty','game','someone','school','those','snow','twurl.nl','gonna','hey','many','start','wait','while','google','finally','everyone','para','try','god','weekend','most','iphone','stuff','around','music','looks','may','thought','keep','yet','reading','must','which','same','real','follow','bit','hours','might','actually','online','job','friends','said','obama','coffee','hate','hard','soon','tweet','por','making','wish','call','movie','tell','thinking','via','site','facebook','few','found','these','tv','sorry','through','already','lot','makes','give','put','waiting','stop','play','says','away','coming','early','dinner','phone','cold','using','times','book','kids','went','nothing','every','years','top','office','friend','talk','feeling','hour','head','web','food','amazing','car','lost','end','girl','since','guess','lunch','hot','sounds','b','funny','idea','glad','saw','hear','mean','name','damn','myself','guy','song','yay','least','business','run','place','friday','buy','enough','anything','late','photo','party','link','interesting','used','shit','tired','internet','following','left','guys','money','far','own','seems','media','baby','class','x','social','seen','miss','forward','part','until','open','win','hi','almost'], languages=['en'])