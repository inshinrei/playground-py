import matplotlib.pyplot as plt
import numpy as np
import seaborn

seaborn.set()

from skimage import data, color, feature
import skimage.data

image = color.rgb2gray(data.chelsea())
hog_vec, hog_vis = feature.hog(image, visualise=True)
fig, ax = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(xticks=[], yticks=[]))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('input')
ax[1].imshow(hog_vis)
ax[1].set_title('HOG features')

from sklearn.datasets import fetch_lfw_people
