import tweepy
from textblob import TextBlob
import re
##try:
consumer_key ='lePEiH8TJUBmgcqtGXkyDH6vW'
consumer_secret = 'STD5DQSCv66iGM4Ep8HyEsScbLvhZd9mLoceGZ9Qp5Rhrb3bHd'

access_token = '2901217459-D31mI2dBzQrETXzgnKSUPMFzU3EM3Z7DdQ9kR0h'
access_token_secret = '4yMXQPBxmHxcbwJ5RpbTdOdz3FHzWUHUSmcT0BT0ZBsyx'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
news_query ="Texas bombing suspect blows self up as police close in, official says"
public_tweets = api.search(q=news_query,lang='en',show_user='false',rpp=100)

for tweet in public_tweets:
    print(tweet.text)
    
    
##        analysis = TextBlob(tweet.text)
##        print(analysis.sentiment)
##except:
##    pass
