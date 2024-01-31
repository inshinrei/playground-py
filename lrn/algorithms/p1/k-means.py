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

from sklearn.cluster import SpectralClustering

model = SpectralClustering(n_clusters=2, offinity='nearest_neighbors', assign_labels='kmeans')
labels = model.fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')

from sklearn.datasets import load_digits

digits = load_digits()

kmeans = KMeans(n_clusters=10, random_state=0)
clusters = kmeans.fit_predict(digits.data)
fig, ax = plt.subplots(2, 5, figsize=(8, 3))
centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(ax.flat, centers):
    axi.set(xticks=[], yticks=[])

from scipy.stats import mode

labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    labels[mask] = mode(digits.target[mask])[0]

from sklearn.metrics import accuracy_score

accuracy_score(digits.target, labels)
from sklearn.metrics import confusion_matrix

mat = confusion_matrix(digits.target, labels)
seaborn.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=digits.target_names,
                yticklabels=digits.target_names)
