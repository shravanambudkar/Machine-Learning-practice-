import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
#z=input('enter the year you need to predict')
df=pd.read_csv('Book1.csv')
# print(df)
plt.scatter(df.year,df.capita)
# plt.show()
reg=linear_model.LinearRegression()
reg.fit(df[['year']],df.capita)
b=reg.predict([[2020]])
print(b)
plt.scatter(df.year,df.capita,color='red',marker='+')
plt.plot(df.year,reg.predict(df[['year']]),color='blue')
plt.show()
