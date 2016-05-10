#First test of Tweepy API
#Based on http://docs.tweepy.org/en/v3.5.0/api.html
import tweepy
import requests

auth = tweepy.OAuthHandler("0h7jv4PcQC5OImXLGNivhmpPp", "qQEVbSDX3WSfxfSXxItXTdX5nZLrrE0YINNrLrTbQEekencQTY")
auth.set_access_token("701559036215431168-2Ln53aAlMZZUFL74hK3BlOCW2f7vEaO", "iUTgwVXYHcZwf3nq0Bpu98qpIQWMzLuQiScgWvpf19hFK")
api = tweepy.API(auth)

user = api.get_user(701559036215431168)

print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text