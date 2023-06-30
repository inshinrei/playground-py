import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

plt.style.use('seaborn-whitegrid')

rng = np.random.RandomState(0)
# for m in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
# plt.plot(rng.rand(5), rng.rand(5), m, label='marker={0}'.format(m))
# plt.legend(numpoints=1)
# plt.xlim(0, 1.8)
# plt.show()

x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.show()
