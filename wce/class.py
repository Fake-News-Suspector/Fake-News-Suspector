import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import  TfidfVectorizer, HashingVectorizer
from sklearn.model_selection import train_test_split
import csv
from sklearn.linear_model import PassiveAggressiveClassifier, SGDClassifier
from sklearn.svm import LinearSVC
from sklearn import metrics
import matplotlib.pyplot as plt



class vector():
	data=["1","MK Stalin Files Police Complaint Against Fake Tweets in His Name","hey","Real"]
	with open("real4.csv",'a') as w:
		writer = csv.writer(w)
		writer.writerow(data)
	w.close()



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
	print(pred)
	print("accuracy:   %0.3f" % score)

	
	