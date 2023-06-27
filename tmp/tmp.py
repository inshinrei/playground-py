import numpy as np


def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x


print(selection_sort(np.array([2, 1, 4, 3, 5])))


def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x


print(bogosort(np.array([2, 1, 4, 3, 5])))
