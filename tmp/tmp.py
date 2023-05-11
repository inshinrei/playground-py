import numpy as np

np.random.seed(0)


def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


vs = np.random.randint(1, 10, size=5)
print(compute_reciprocals(vs))
