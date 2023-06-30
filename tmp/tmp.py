import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from sklearn.gaussian_process import GaussianProcessClassifier

plt.style.use('seaborn-whitegrid')

# rng = np.random.RandomState(0)
# for m in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
# plt.plot(rng.rand(5), rng.rand(5), m, label='marker={0}'.format(m))
# plt.legend(numpoints=1)
# plt.xlim(0, 1.8)
# plt.show()

# x = rng.randn(100)
# y = rng.randn(100)
# colors = rng.rand(100)
# sizes = 1000 * rng.rand(100)
#
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
# plt.show()

# x = np.linspace(0, 10, 50)
# dy = 0.8
# y = np.sin(x) + dy * np.random.randn(50)
# plt.errorbar(x, y, yerr=dy, fmt='.k')
# plt.show()

model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = data = model(xdata)

gp = GaussianProcessClassifier(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1, random_start=100)
gp.fit(xdata[:, np.newaxis], ydata)

xfit = np.linspace(0, 10, 1000)
yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
dyfit = 2 * np.sqrt(MSE)

plt.plot(xdata, ydata, 'or')
plt.plot(xfit, yfit, '-', color='gray')
plt.fill_between(xfit, yfit - dyfit, yfit + dyfit, color='gray', alpha=0.2)
plt.xlim(0, 10)
plt.show()
