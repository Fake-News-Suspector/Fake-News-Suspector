import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import  TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split
import csv
from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup 
from newspaper import Article 



class cate():
	
	def scat(sstring):
		# https://www.yahoo.com/news/gop-lawmaker-knocks-trump-putin-call-refuses-distance-president-135204872.html
		url= sstring
		category=['Business','Politics','Health','Entertainment','Lifestyle','Finance','Celebrity','Science','Technology','Food','Sport','World']
		flag=0
		for i in category:
			if(i.lower() in url.lower()):
				flag=1
				cat=i
				break
		if(flag==1):
			return cat
		else:


			data1=[]
			try:
				article = Article(url)
				article.download()
				article.html
				article.parse()
				data1.append('100')
				data1.append(article.title)
				
		        # with open('real4.csv','a') as w:
		        #     writer = csv.writer(w)
		        #     writer.writerow(data)
		        # w.close()
				data=[None]*2
				data[0]=data1[1]
				data[1]=""
				# with open("home/category4.csv",'a') as w:
				with open("home/final2.csv",'a') as w:				
					writer = csv.writer(w)
					writer.writerow(data)
				w.close()

				df=pd.read_csv("home/final2.csv")


				# y=df.category
				


				
				
				# df=df.drop('category',axis=1)

				
				X=np.array(df['title'])
				y=np.array(df['label'])

				X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.00022,shuffle=False)
				# print(X_train)
				# print(y_train)
				

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
				# score = metrics.accuracy_score(y_test, pred)
				print(pred[0])
				return pred[0]        
			except Exception as e:
				
				pass



	
	# print("accuracy:   %0.3f" % score)

		



# ---------------------previous--------------------------------------------------------------------------------------------------------------------
		# df=pd.read_csv("/home/devansh/Documents/wce/fakenews/home/category4.csv")
		# print(len(df))
		
		# # y=df.category
		


		
		
		# # df=df.drop('category',axis=1)

		
		# X=np.array(df.drop('category',1))
		# y=np.array(df['category'])

		# X_train,X_test,y_train,y_test=train_test_split(df['title'],y,test_size=0.0007)
		# # print(X_train)
		# # print(y_train)
		

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
		# return pred[0]
	

		
	