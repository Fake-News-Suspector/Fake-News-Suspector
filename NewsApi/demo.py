import pandas as pd
import tweepy
import csv
import re
import nltk
import numpy as np

consumer_key ='Q0TaSR4O9Tt1Rvsqs9xzfiJhi'
consumer_secret = 'aPcZOX0XLLDLAjbd749sFgZ6ir09rNkJfCq0a2oP0PdulGiQlv'

access_token = '976437531419004928-b3iXFrfNVfUtZNlXB8dLaIWRhdqQaP1'
access_token_secret = 'M8o0Xs41krq0zZPKIiisCsH1bEYsSHWk7J34jO02oCZKO'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
df = pd.read_csv('C:/Users/PRIYAM SHAH/Fake-News-Suspector/codes/yahoo.csv')
for i in df.title:
    news_query = i
    news_keywords=[token for token, pos in nltk.pos_tag(nltk.word_tokenize(news_query)) if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
    print(news_keywords)
    propernouns = [word for word,pos in nltk.pos_tag(nltk.word_tokenize(news_query)) if pos == 'NNP']
    print(propernouns)
    public_tweets = api.search(q=news_query,lang='en',show_user='false',rpp=100)
    ls=[]
    data=[None]*2
    data[0]=news_query
    if(len(propernouns)>0):
        
        for tweet in public_tweets:
            count=0
            count1=0
            for k in propernouns:
                result1 = re.serach(k,tweet.text)
                if result1!=None:
                    count1=count1+1
            if(count1==len(propernouns)):
                for j in news_keywords:
                    result = re.search(j,tweet.text)
                    if result!=None:
                        count=count+1
                Match_percent = (count/len(news_keywords))
                ls.append(Match_percent)
                with open('Learned.csv','a',encoding='UTF-8') as w:
                    writer = csv.writer(w)
                    data[1]=np.mean(ls)
                    print(data[1])
                    writer.writerow(data)
                w.close()
            else:
                continue
            
    else:
        for tweet in public_tweets:
            count=0
            for j in news_keywords:
                result = re.search(j,tweet.text)
                if result!=None:
                    count=count+1
            Match_percent = (count/len(news_keywords))
            ls.append(Match_percent)
        with open('Learned.csv','a',encoding='UTF-8') as w:
            writer = csv.writer(w)
            data[1]=np.mean(ls)
            print(data[1])
            writer.writerow(data)
        w.close()



