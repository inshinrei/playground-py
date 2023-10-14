import matplotlib.pyplot as plt
import numpy as np
import seaborn

seaborn.set()

from sklearn.datasets import make_blobs

X, y_true = make_blobs(n_samples=400, centers=4, cluster_std=0.60, random_state=0)
X = X[:, ::-1]
from sklearn.cluster import KMeans

kmeans = KMeans(4, random_state=0)
labels = kmeans.fit(X).predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')

from scipy.spatial.distance import cdist


def plot_kmeans(_kmeans, _X, ax=None):
    _labels = _kmeans.fit_predict(_X)
    ax = ax or plt.gca()
    ax.axis('eq')
    ax.scatter(_X[:, 0], _X[:, 1], c=_labels, s=40, cmap='viridis', zorder=2)
    _centers = _kmeans.cluster_centers_
    radii = [cdist(_X[_labels == i], [center]).max() for i, center in enumerate(_centers)]
    for c, r in zip(_centers, radii):
        ax.add_patch(plt.Circle(c, r, fc='#CCCCCC', lw=4, alpha=0.5, zorder=1))


kmeans = KMeans(n_clusters=4, random_state=0)
plot_kmeans(kmeans, X)

rng = np.random.RandomState(13)
X_stretched = np.dot(X, rng.randn(2, 2))
kmeans = KMeans(n_clusters=4, random_state=0)
plot_kmeans(kmeans, X_stretched)
