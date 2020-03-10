from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score



digits = load_digits()


X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.3)

#LogiaticRwg

lr = LogisticRegression(solver='liblinear',multi_class='ovr')
lr.fit(X_train, y_train)
lr.score(X_test, y_test)

#SVM

svm = SVC(gamma='auto')
svm.fit(X_train, y_train)
svm.score(X_test, y_test)

#Random Forest

rf = RandomForestClassifier(n_estimators=40)
rf.fit(X_train, y_train)
rf.score(X_test, y_test)

##########Using Cross K fold


cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr'), digits.data, digits.target,cv=3)

cross_val_score(SVC(gamma='auto'), digits.data, digits.target,cv=3)

cross_val_score(RandomForestClassifier(n_estimators=40),digits.data, digits.target,cv=3)


#Parameter tunning using k fold cross validation


scores1 = cross_val_score(RandomForestClassifier(n_estimators=5),digits.data, digits.target, cv=10)
np.average(scores1)


scores2 = cross_val_score(RandomForestClassifier(n_estimators=20),digits.data, digits.target, cv=10)
np.average(scores2)


scores3 = cross_val_score(RandomForestClassifier(n_estimators=30),digits.data, digits.target, cv=10)
np.average(scores3)
