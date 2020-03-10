import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC







iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()
df['target'] = iris.target
df.head()


X = df.drop(['target'], axis='columns')
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = SVC()
model.fit(X_train, y_train)
model.score(X_test, y_test)
#model.predict([[4.8,3.0,1.5,0.3]])