# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import linear_model
# import math
# from word2number import w2n
# #z=input('enter the year you need to predict')
# df=pd.read_csv('ex2.csv')
# # print(df)
# reg=linear_model.LinearRegression()
# # reg.fit([['']])
# zero=0
# df.experience=df.experience.fillna("zero")
# df.experience=df.experience.apply(w2n.word_to_num)
# # print(df)
# avg_test=math.floor(df.test_score.median())
# df.test_score=df.test_score.fillna(avg_test)
# print(df)
# reg.fit(df[['experience','test_score','interview_score']],df.salary)
# print(reg.predict([[12,10,10]]))
# # a=np.linspace(0,36,36)
# b=np.array(a)
# b.reshape(6,6)
# print(b)
# b.reshape(36)[::7]
# print(x)
b=2
a= b*b
print(a)