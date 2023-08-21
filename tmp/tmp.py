import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib as mpl
import seaborn as sns
from sklearn.datasets import fetch_olivetti_faces

ax = plt.axes(axisbg='#e6e6e6')
ax.set_axisbelow(True)
plt.grid(color='w', linestyle='solid')
for s in ax.spines.values():
    s.set_visible(False)
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.tick_params(colors='gray', direction='out')
for tick in ax.get_xticklabels():
    tick.set_color('gray')


def hist_and_lines():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(['a', 'b', 'c'], loc='lower left')
