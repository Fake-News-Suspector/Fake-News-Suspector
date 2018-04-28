import pprint
from newsapi import NewsApiClient
import sqlite3
import re
import nltk
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GOOGLE NEWS API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class search():
   
   def apicall(sstring):
      ls=[]
      newsapi = NewsApiClient(api_key='d6bcc880b0234b1abaeadd0acaabc57a')
      news_query=sstring
      news_keywords=[token for token, pos in nltk.pos_tag(nltk.word_tokenize(news_query)) if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
      # print(news_keywords)
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
         ls.append(Match_percent)

         if Match_percent < 0.85 :
            con.execute("DELETE FROM RESULT WHERE title LIKE \""+data[5]+"\"")
            con.commit()
         else:
         
            continue

      return ls
   #~~~~~~~~~~~~~~~~~~~To VIEW DATABASE RESULT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   # result = con.execute("SELECT * FROM Result")
       
   # for data in result:
   #    print(str(data[0])+"\n"+str(data[1])+"\n"+str(data[2])+"\n"+str(data[3])+"\n"+str(data[4])+"\n"+str(data[5])+"\n"+str(data[6])+"\n"+str(data[7])+"\n")

   # con.close()
