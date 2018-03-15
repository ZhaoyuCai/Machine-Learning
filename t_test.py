import numpy as np
from scipy import stats

N = 10
a = np.random.randn(N) + 2
b = np.random.randn(N)

var_a = a.var(ddof=1) #“Delta Degrees of Freedom”:
                    # the divisor used in the calculation is N - ddof,
                    # where N represents the number of elements. By default ddof is zero.
var_b = b.var(ddof=1)

s = np.sqrt((var_a + var_b) / 2)
t = (a.mean() - b.mean()) / (s * np.sqrt((2.0/N)))
df = 2*N - 2
p = 1 - stats.t.cdf(t, df=df)
print("t:\t", t, "p:\t", 2*p)

t2, p2 = stats.ttest_ind(a, b) # ind is for independent
print("t2:\t", t2, "p2:\t", p2) # same result