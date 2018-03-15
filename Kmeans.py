import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist

def Kmeans(X, k=3, max_iter=100):
    n, m = X.shape
    centroids = X[np.random.choice(range(n), size=k, replace=False), :]
    centroids_next = np.zeros(centroids.shape)

    for _ in range(max_iter):

        C = np.zeros(n)

        for i in range(n):
            dist = np.zeros(k)
            for c in range(k):
                dist[c] = np.linalg.norm(centroids[c,:] - X[i,:])
            C[i] = np.argmin(dist)
        # X['Class'] = C
        # print(X[C==0].mean(axis=0))
        centroids_next = np.array([X[C==c].mean(axis=0) for c in range(k)])

        if centroids.all == centroids_next.all:
            break

        centroids = centroids_next

    return C


X = pd.read_csv("iris.csv", header=None)
X = X[list(range(X.shape[1]-1))]
X = np.array(X)

print(Kmeans(X, k=3))