import numpy as np

from sklearn.datasets import fetch_20newsgroups
d = fetch_20newsgroups()
l = d.target_names

categories = ['comp.graphics', 'rec.autos', 'talk.religion.misc']
train = fetch_20newsgroups(subset='train', categories=categories)  #sklearn.utils.Bunch
test = fetch_20newsgroups(subset='test', categories=categories)

X = Xtrain = train.data
y = ytrain = ytrue = train.target
Xtest = test.data
ytest = test.target

m = 100     # use m datapoints only
X = X[:m]
y = y[:m]   # roughly the same class proportion
