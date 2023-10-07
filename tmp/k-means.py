import matplotlib.pyplot as plt
import numpy as np
import seaborn

seaborn.set()

from sklearn.datasets._samples_generator import make_blobs

X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=50)

from sklearn.cluster import KMeans

k_means = KMeans(n_clusters=4)
k_means.fit(X)
y_kmeans = k_means.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

from sklearn.metrics import pairwise_distances_argmin


def find_clusters(X, n_clusters, seed=2):
    rng = np.random.RandomState(seed)
    i = rng.permutation(X.shape[0])[:n_clusters]
    _centers = X[i]
    while True:
        labels = pairwise_distances_argmin(X, centers)
        new_centers = np.array([X[labels == i].mean(0) for i in range(n_clusters)])
        if np.all(_centers == new_centers):
            break
        _centers = new_centers
    return _centers, labels


centers, labels = find_clusters(X, 4)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')

from sklearn.datasets import make_moons

X, y = make_moons(200, noise=.05, random_state=0)
labels = KMeans(2, random_state=0).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
