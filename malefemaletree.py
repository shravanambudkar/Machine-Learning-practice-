from sklearn import tree

#creating a first variable dataset

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#creating labels according to the dataset

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

#creating a classifier using decisiontree

classi= tree.DecisionTreeClassifier()

lol = classi.fit(X,Y)

#predicting the dataset

prediction = lol.predict([[160,60,38]])
print (prediction)