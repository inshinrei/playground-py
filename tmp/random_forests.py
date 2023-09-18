import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=300, centers=4, random_state=0, cluster_std=1.0)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow')

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier().fit(X, y)


def visualize_classifier(model, X, y, ax=None, cmap='rainbow'):
    ax = ax or plt.gca()
    ax.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=cmap, clim=(y.min(), y.max()), zorder=3)
    ax.axis('tight')
    ax.axis('off')
    x_lim = ax.get_xlim()
    y_lim = ax.get_ylim()
    model.fit(X, y)
    xx, yy = np.meshgrid(np.linspace(*x_lim, num=200), np.linspace(*y_lim, num=200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    n_classes = len(np.unique(y))
    ax.contourf(xx, yy, Z, alpha=0.3, levels=np.arange(n_classes + 1) - 0.5, cmap=cmap, clim=(y.min(), y.max()),
                zorder=1)
    ax.set(xlim=x_lim, ylim=y_lim)


visualize_classifier(DecisionTreeClassifier(), X, y)
