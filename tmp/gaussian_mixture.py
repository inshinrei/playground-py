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

from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=4).fit(X)
labels = gmm.predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
probs = gmm.predict_proba(X)
size = 50 * probs.max(1) ** 2
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=size)

from matplotlib.patches import Ellipse


def draw_ellipse(position, covariance, ax=None, **kwargs):
    ax = ax or plt.gca()
    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd(covariance)
        angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
        width, height = 2 * np.sqrt(s)
    else:
        angle = 0
        width, height = 2 * np.sqrt(covariance)
    for nsig in range(1, 4):
        ax.add_patch(Ellipse(position, nsig * width, nsig * height, angle, **kwargs))


def plot_gmm(_gmm, _X, label=True, ax=None):
    ax = ax or plt.gca()
    _labels = _gmm.ftt(_X).predict(_X)
    if label:
        ax.scatter(_X[:, 0], _X[:, 1], c=_labels, s=40, cmap='viridis', zorder=2)
    else:
        ax.scatter(_X[:, 0], _X[:, 1], s=40, zorder=2)
    ax.axis('equal')
    w_factor = 0.2 / _gmm.weights_.max()
    for pos, covar, w in zip(_gmm.means_, _gmm.covars_, _gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)


gmm = GaussianMixture(n_components=4, random_state=42)
plot_gmm(gmm, X)

from sklearn.datasets import make_moons

Xmoon, ymoon = make_moons(200, noise=.05, random_state=0)
plt.scatter(Xmoon[:, 0], Xmoon[:, 1])
gmm2 = GaussianMixture(n_components=2, covariance_type='full', random_state=0)
plot_gmm(gmm2, Xmoon)

gmm16 = GaussianMixture(n_components=16, covariance_type='full', random_state=0)
plot_gmm(gmm16, Xmoon, label=False)

Xnew = gmm16.sample(400, random_state=42)
plt.scatter(Xnew[:, 0], Xnew[:, 1])
