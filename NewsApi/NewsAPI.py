from newsapi import NewsApiClient
import csv
import re
import nltk
import numpy as np

def read():
    with open('test.csv',  "rt", encoding='utf8') as f:
        reader = csv.reader(f)
        for row in reader:
            news_query=row[1]
            
            api(news_query)

def api(news_query):
    newsapi = NewsApiClient(api_key='d6bcc880b0234b1abaeadd0acaabc57a')
    news_keywords=[token for token, pos in nltk.pos_tag(nltk.word_tokenize(news_query)) if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
    print(news_keywords)
    #news_keywords=news_query.split(" ")
    all_articles = newsapi.get_everything(q=news_query)
    ls=[]
    search(all_articles,ls,news_keywords)
def search(all_articles,ls,news_keywords):
    for i in all_articles['articles']:
        count=0
        for j in news_keywords:
            result=re.search(j,str(i['title'])
            if(result != None):
                             count=count+1               
            Match_percent =(count/len(news_keywords))
            ls.append(Match_percent)
    if(np.mean(ls) > 0.5):
        print('REAL')
        with open('test.csv','wt',encoding='utf8') as w:
                writer = csv.writer(w)
                data[4]='1'
                writer.writerow(data)
    else:
        print('Fake')
        with open('test.csv','wt',encoding='utf8') as w:
                writer = csv.writer(w)
                data[4]='0'
                writer.writerow(data)
w.close()
f.close()
read()
