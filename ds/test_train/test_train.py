import random
from typing import TypeVar, List, Tuple

X = TypeVar('X')


def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    data = data[:]
    random.shuffle(data)

    cut = int(len(data) * prob)
    return data[:cut], data[cut:]
