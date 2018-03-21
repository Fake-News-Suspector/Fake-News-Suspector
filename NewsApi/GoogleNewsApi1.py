import pprint
from newsapi import NewsApiClient
import sqlite3
import re
import nltk
from rake_nltk import Rake
import tweepy
from textblob import TextBlob
import praw

newsapi = NewsApiClient(api_key='d6bcc880b0234b1abaeadd0acaabc57a')
news_query='Donald Trump almost died'
news_keywords=[token for token, pos in nltk.pos_tag(nltk.word_tokenize(news_query)) if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
print(news_keywords)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RAKE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
r=Rake()
r.extract_keywords_from_text(news_query)
s = r.get_word_degrees()
print(s)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GOOGLE NEWS API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#news_keywords=news_query.split(" ")
all_articles = newsapi.get_everything(q=news_query)

#~~~~~~~~~~~~~~~~~~~~Twitter API~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~```

try:
    consumer_key ='lePEiH8TJUBmgcqtGXkyDH6vW'
    consumer_secret = 'STD5DQSCv66iGM4Ep8HyEsScbLvhZd9mLoceGZ9Qp5Rhrb3bHd'

    access_token = '2901217459-D31mI2dBzQrETXzgnKSUPMFzU3EM3Z7DdQ9kR0h'
    access_token_secret = '4yMXQPBxmHxcbwJ5RpbTdOdz3FHzWUHUSmcT0BT0ZBsyx'

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)
    
    public_tweets = api.search(q=news_query,lang='en',show_user='false',rpp=100)

##    for tweet in public_tweets:
##        print(tweet.text)
##        analysis = TextBlob(tweet.text)
##        print(analysis.sentiment)
except:
    pass
#~~~~~~~~~~~~~~~~~~~~~~~~~REDDIT API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


reddit = praw.Reddit(client_id = 'NCGfJ_dLCKkLeQ',
                     client_secret = '-pzdUANPZk9hdNfXUlKAOuvvzHw',
                     username = 'priyamshah112',
                     password = '7738478888a',
                     user_agent='newsscrapper')

try:    
    news_query = 'Trip wire may have set off bomb in Austin, wounding two men: police'
    all = reddit.subreddit("all")
##    for i in all.search(news_query, limit=100):
##        print (i.title)
##        print(i.url)

except:
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DATABASE STORAGE OF JSON RESULT FROM GOOGLE API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

con = sqlite3.connect('Result.db')
#myFile = open('Result.txt', 'w')
con.execute("DROP TABLE IF EXISTS Result")
con.execute("CREATE TABLE Result (author BLOB,description BLOB,publishedAt BLOB,source_id BLOB,source_name BLOB,title BLOB,url BLOB,urlToImage BLOB)")
for i in all_articles['articles']:
   #myFile.write("author "+str(i['author'])+"\n"+"description "+str(i['description'])+"\npublishedAt "+str(i['publishedAt'])+"\n"+"source \n"+str(i['source']['id'])+"\nsource\n "+str(i['source']['name'])+"\ntitle "+str(i['title'])+"\nurl "+str(i['url'])+'\nurlToImage '+str(i['urlToImage']))
   con.execute("INSERT INTO Result(author,description,publishedAt,source_id,source_name,title,url,urlToImage) VALUES (?,?,?,?,?,?,?,?)" , (i['author'],i['description'],i['publishedAt'],i['source']['id'],i['source']['name'],i['title'],i['url'],i['urlToImage']))
for i in all.search(news_query, limit=100):
   con.execute("INSERT INTO Result(title,url) VALUES (?,?)",(i.title,i.url))
for tweet in public_tweets:
    con.execute("INSERT INTO Result")
con.commit()
#~~~~~~~~~~~~~~~~~~~~REGEX OVER TITLE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
result = con.execute("SELECT * FROM Result")
for data in result:
    r.extract_keywords_from_text(str(data[5]))
    d = r.get_word_degrees()
    for i,j in s:
        if i==d
   


#~~~~~~~~~~~~~~~~~~~To VIEW DATABASE RESULT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
result = con.execute("SELECT * FROM Result")
    
for data in result:
   print(str(data[5]))

con.close()
