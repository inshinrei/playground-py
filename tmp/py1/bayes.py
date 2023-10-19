import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

from sklearn.datasets import make_blobs

X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X, y)
rng = np.random.RandomState(0)
X_new = [-6, -14] + [14, 18] * rng.rand(2000, 2)
# y_new = model.predict(X_new)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
lim = plt.axis()
plt.scatter(X_new[:, 0], X_new[:, 1], c=y_new, s=20, cmap='RdBu', alpha=0.1)
plt.axis(lim)

y_prob = model.predict_proba(X_new)
y_prob[-8:].round(2)

from sklearn.datasets import fetch_20newsgroups

data = fetch_20newsgroups()
categories = ['talk.religion.misc', 'soc.religion.christian', 'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

m_model = make_pipeline(TfidfVectorizer(), MultinomialNB())
m_model.fit(train.data, train.target)
labels = m_model.predict(test.data)

from sklearn.metrics import confusion_matrix

mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=train.target_names,
            yticklabels=train.taret_names)
plt.xlabel('as is l')
plt.ylabel('predicted l')


def predict_cat(s, _train=train, _model=m_model):
    p = _model.predict([s])
    return _train.target_names[p[0]]
