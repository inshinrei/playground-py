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

from sklearn.ensemble import BaggingClassifier

tree = DecisionTreeClassifier()
bag = BaggingClassifier(tree, n_estimators=100, max_samples=0.8, random_state=1)
bag.fit(X, y)
visualize_classifier(bag, X, y)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=0)
visualize_classifier(model, X, y)

rng = np.random.RandomState(42)
x = 10 * rng.rand(200)


def get_model(x, sigma=0.3):
    fast_oscillation = np.sin(5 * x)
    slow_oscillation = np.sin(0.5 * x)
    noise = sigma * rng.randn(len(x))
    return slow_oscillation + fast_oscillation + noise


from sklearn.ensemble import RandomForestRegressor

forest = RandomForestRegressor(200)
forest.fit(x[:, None], y)
x_fit = np.linspace(0, 10, 1000)
y_fit = forest.predict(x_fit[:, None])
y_true = get_model(x_fit, sigmna=0)
plt.errorbar(x, y, 0.3, fmt='o', alpha=0.5)
plt.plot(x_fit, y_fit, '-r')
plt.plot(x_fit, y_true, '-k', alpha=0.5)
