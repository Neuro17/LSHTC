from sklearn.datasets import load_svmlight_file
from sklearn import neighbors
import pprint as pp

X,y = load_svmlight_file("resource/my_train.csv", multilabel = True)

print X
print X[:, 0]
n_neighbors = 3
# for weights in ['uniform', 'distance']:
#     # we create an instance of Neighbours Classifier and fit the data.
#     clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
#     clf.fit(X, y)