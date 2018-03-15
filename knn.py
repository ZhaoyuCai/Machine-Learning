import numpy as np
from numpy.linalg import norm
from heapq import heappush, heappop
from collections import Counter

N, D = 20, 2
K = 3

X = np.random.random((N, D))
Y = np.random.choice([0,1], size = N)
new_p = np.random.random(D)

#print(X)
#print(Y)


def kNN(x, y, p, k = 3):
	n, d = x.shape
	dist_class = [(-norm(x[i] - p), y[i]) for i in range(n)]

	top_k = []

	for d_c in dist_class:
		#print(d_c)
		heappush(top_k, d_c)
		if len(top_k) > k:
			heappop(top_k)

	top_c = []

	for i in range(k):
		top_c.append(heappop(top_k)[-1])

	print(top_c)

	counter = Counter(top_c)

	if counter[1] > counter[0]:
		return 1
	elif counter[1] < counter[0]:
		return 0
	else:
		return 1 - top_c[-1]

print(kNN(x = X, y = Y, p = new_p, k = 4))