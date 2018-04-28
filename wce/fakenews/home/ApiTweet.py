import tweepy
import re
import nltk
import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import  TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split
import math
from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics
import matplotlib.pyplot as plt
import csv


class twitter():
    def tweet(sstring):
        
        
        consumer_key ='Q0TaSR4O9Tt1Rvsqs9xzfiJhi'
        consumer_secret = 'aPcZOX0XLLDLAjbd749sFgZ6ir09rNkJfCq0a2oP0PdulGiQlv'

        access_token = '976437531419004928-b3iXFrfNVfUtZNlXB8dLaIWRhdqQaP1'
        access_token_secret = 'M8o0Xs41krq0zZPKIiisCsH1bEYsSHWk7J34jO02oCZKO'

        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)

        api = tweepy.API(auth)

        news_query = sstring
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
        
        
            #classication




        data=["1",sstring,"hey","Real"]
        with open("/home/devansh/Documents/wce/fakenews/home/real5.csv",'a') as w:
            writer = csv.writer(w)
            writer.writerow(data)
        w.close()
        
        df=pd.read_csv("/home/devansh/Documents/wce/fakenews/home/real5.csv")
    
    
        y=df.label
    
    
    
        df=df.drop('label',axis=1)

        X_train,X_test,y_train,y_test=train_test_split(df['title'],y,test_size=0.00048,shuffle=False)
        print(X_train)
        print(y_train)
    

        tfidf_vectorizer=TfidfVectorizer(stop_words='english',max_df=0.7)
        tfidf_train=tfidf_vectorizer.fit_transform(X_train)
        tfidf_test=tfidf_vectorizer.transform(X_test)
    

    # pa_tfidf_clf = PassiveAggressiveClassifier(n_iter=50)
    # pa_tfidf_clf.fit(tfidf_train, y_train)
    # pred = pa_tfidf_clf.predict(tfidf_test)
    # print(pred)



        svc_tfidf_clf = LinearSVC()
        svc_tfidf_clf.fit(tfidf_train, y_train)
        pred = svc_tfidf_clf.predict(tfidf_test)
        score = metrics.accuracy_score(y_test, pred)
        print(pred)
        print("accuracy:   %0.3f" % score)
        ls1=[]
        # e=1/(1+math.exp(-((0.90*np.mean(ls))+0.12924)))
        e=(0.90*np.mean(ls))+0.12924
        ls1.append(e)
        # ls1.append(pred[0])
        return (e*100)
    

    
    

    

        
        # df=pd.read_csv("/home/devansh/Documents/wce/fakenews/home/real5.csv")
        
        
        # y=df.label
        
        
        
        # df=df.drop('label',axis=1)

        # X_train,X_test,y_train,y_test=train_test_split(df['title'],y,test_size=0.00048,shuffle=False)
        # print(X_train)
        # print(y_train)
        

        # tfidf_vectorizer=TfidfVectorizer(stop_words='english',max_df=0.7)
        # tfidf_train=tfidf_vectorizer.fit_transform(X_train)
        # tfidf_test=tfidf_vectorizer.transform(X_test)
        

        # # pa_tfidf_clf = PassiveAggressiveClassifier(n_iter=50)
        # # pa_tfidf_clf.fit(tfidf_train, y_train)
        # # pred = pa_tfidf_clf.predict(tfidf_test)
        # # print(pred)



        # svc_tfidf_clf = LinearSVC()
        # svc_tfidf_clf.fit(tfidf_train, y_train)
        # pred = svc_tfidf_clf.predict(tfidf_test)
        # score = metrics.accuracy_score(y_test, pred)
        # ls1=[]
        # e=1/(1+math.exp(-((0.90*np.mean(ls))+0.12924)))
        # #e=(0.90*np.mean(ls))+0.12924
        # ls1.append(e)
        # ls1.append(pred[0])
        # return ls1
    
