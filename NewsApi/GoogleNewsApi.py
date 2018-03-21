import pprint
from newsapi import NewsApiClient
import sqlite3
import re
import nltk
from rake_nltk import Rake
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GOOGLE NEWS API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


newsapi = NewsApiClient(api_key='d6bcc880b0234b1abaeadd0acaabc57a')
news_query='Donald Trump almost died'
news_keywords=[token for token, pos in nltk.pos_tag(nltk.word_tokenize(news_query)) if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
print(news_keywords)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RAKE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
r=Rake()
r.extract_keywords_from_text(news_query)
s = r.get_word_degrees()

#news_keywords=news_query.split(" ")
all_articles = newsapi.get_everything(q=news_query)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DATABASE STORAGE OF JSON RESULT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

con = sqlite3.connect('Result.db')
#myFile = open('Result.txt', 'w')
con.execute("DROP TABLE IF EXISTS Result")
con.execute("CREATE TABLE Result (author BLOB,description BLOB,publishedAt BLOB,source_id BLOB,source_name BLOB,title BLOB,url BLOB,urlToImage BLOB)")
for i in all_articles['articles']:
   #myFile.write("author "+str(i['author'])+"\n"+"description "+str(i['description'])+"\npublishedAt "+str(i['publishedAt'])+"\n"+"source \n"+str(i['source']['id'])+"\nsource\n "+str(i['source']['name'])+"\ntitle "+str(i['title'])+"\nurl "+str(i['url'])+'\nurlToImage '+str(i['urlToImage']))
   con.execute("INSERT INTO Result(author,description,publishedAt,source_id,source_name,title,url,urlToImage) VALUES (?,?,?,?,?,?,?,?)" , (i['author'],i['description'],i['publishedAt'],i['source']['id'],i['source']['name'],i['title'],i['url'],i['urlToImage']))
con.commit()
#~~~~~~~~~~~~~~~~~~~~REGEX OVER TITLE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
result = con.execute("SELECT * FROM Result")
for data in result:
   count=0
   for i in news_keywords:
      result=re.search(i,str(data[5]))
      if result!=None:
         count=count+1               
   Match_percent=(count/len(news_keywords))
   print(Match_percent)


#~~~~~~~~~~~~~~~~~~~To VIEW DATABASE RESULT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
result = con.execute("SELECT * FROM Result")
    
for data in result:
   print(str(data[5]))

con.close()

#pprint.pprint(all_articles)
"""
Example of Attributes Searches over 30k+ news sites
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_parameter='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
"""

