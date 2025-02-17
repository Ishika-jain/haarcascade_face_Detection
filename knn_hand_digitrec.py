# -*- coding: utf-8 -*-
"""KNN_hand_digitrec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10iLiFVbi4IfjykENVf6uCrvBxqms-2KO
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import  make_blobs
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = np.load('/content/mnist_train_small.npy')

X = data[:, 1:]
X.shape

y=data[:, 0]

plt.imshow(X[0].reshape(28,28), cmap="gray")

#X,y=make_blobs(n_samples=100, centers = 3, random_state=42)
X.shape

#plt.scatter(X[:,0],X[:,1], c=y)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33, random_state=42)

model = KNeighborsClassifier()

model.fit(X_train,y_train)

model.predict(X_test[:10])

y_test[:10]

model.score(X_test,y_test)

X_test.shape

X.shape

plt.imshow(X_test[0].reshape(28,28), cmap="gray")



