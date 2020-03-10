import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv("carprices.csv")
df.head()

X = df[['Mileage','Age(yrs)']]
y = df['Sell Price($)']


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

clf = LinearRegression()
clf.fit(X_train, y_train)

clf.predict(X_test)
clf.score(X_test, y_test)