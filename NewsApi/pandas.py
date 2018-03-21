import pandas as pd
import tweepy
import csv
import re
import nltk
import numpy as np

consumer_key ='lePEiH8TJUBmgcqtGXkyDH6vW'
consumer_secret = 'STD5DQSCv66iGM4Ep8HyEsScbLvhZd9mLoceGZ9Qp5Rhrb3bHd'

access_token = '2901217459-D31mI2dBzQrETXzgnKSUPMFzU3EM3Z7DdQ9kR0h'
access_token_secret = '4yMXQPBxmHxcbwJ5RpbTdOdz3FHzWUHUSmcT0BT0ZBsyx'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
df = pd.read_csv('C:/Users/PRIYAM SHAH/Fake-News-Suspector/NewsApi/tweet.csv')
pf = pd.read_csv('C:/Users/PRIYAM SHAH/Fake-News-Suspector/NewsApi/tweet.csv')

for i in df.title:
    print(i)
    
    news_query = i
    news_keywords=[token for token, pos in nltk.pos_tag(nltk.word_tokenize(news_query)) if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
    print(news_keywords)
    public_tweets = api.search(q=news_query,lang='en',show_user='false',rpp=100)
    ls=[]
    for tweet in public_tweets:
        count=0
        for j in news_keywords:
            result = re.search(j,tweet.text)
            if result!=None:
                count=count+1
        Match_percent = (count/len(news_keywords))
        ls.append(Match_percent)
    print(np.mean(ls))    
    pf.set_value(i,4,np.mean(ls))



