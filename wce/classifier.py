import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import  TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics
import matplotlib.pyplot as plt
import csv


class vector():
	
	def classy():
		data=[None]*3
		with open('real4','a') as t:
			writer=csv.writer(t)
			data[0]=100
			data[1]=sstring
			data[2]="hello world i am priyam"
			writer.writerow(data)
		t.close()
		
		df=pd.read_csv("real4.csv")
		
		
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
		return pred

		
		