
from newsapi import NewsApiClient
import csv
import re
import nltk
import numpy as np
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    
with open('fake_or_real_news.csv',"rt") as f:
    reader = csv.reader(f)
    for row in reader:
        news_query=row[0]
        newsapi = NewsApiClient(api_key='08a809667a1d4fbb90865b286165c822')
        news_keywords=[token for token, pos in nltk.pos_tag(nltk.word_tokenize(news_query)) if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
        all_articles = newsapi.get_everything(q=news_query)
        ls=[]
        data=[None]*5
        data[0]=row[0]
        data[1]=row[1]
        data[2]=row[2]
        data[3]=row[3]
        for i in all_articles['articles']:
               count=0
               for j in news_keywords:
                   
                   result=re.search(j,str(i['title']))
                   if result!=None:
                       count=count+1               
               Match_percent=(count/len(news_keywords))
               ls.append(Match_percent)
   
        with open('test1.csv','a') as w:
            writer = csv.writer(w)
            data[4]=np.mean(ls)
            print(data[4])
            writer.writerow(data)
        w.close()

