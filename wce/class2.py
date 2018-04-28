import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn import datasets, linear_model, metrics



df=pd.read_csv("learn.csv")
	
df=df.dropna(axis=0,how='any')
X=np.array(df.drop('label',1))
y=np.array(df['label'])


	
	


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)


reg = linear_model.LinearRegression()
 

reg.fit(X_train, y_train)
 
# print('Coefficients: \n', reg.coef_)
# print('Coefficients: \n', reg.intercept_)

print('Variance score: {}'.format(reg.score(X_test, y_test)))
