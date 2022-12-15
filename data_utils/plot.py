import math
from collections import Counter
from typing import List, Dict

import matplotlib.pyplot as plt


def bucketsize(point: float, bucket_size: float) -> float:
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points: List[float], bucket_size: float) -> Dict[float, int]:
    return Counter(bucketsize(point, bucket_size) for point in points)


def plot_histogram(points: List[float], bucket_size: float, title: str = ''):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
