import numpy as np

r = np.random.RandomState(42)
x = r.randint(100, size=1000)

print([x[1], x[100], x[233]])
print(np.arange(12).reshape((3, 4)))

mean = [0, 0]
cov = [[1, 2], [2, 5]]
X = r.multivariate_normal(mean, cov, 100)
print(X.shape)
