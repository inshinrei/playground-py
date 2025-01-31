def compare_and_swap(arr: list[int], ind1: int, ind2: int, direction: int) -> None:
    if (direction == 1 and arr[ind1] > arr[ind2]) or (direction == 2 and arr[ind1] < arr[ind2]):
        arr[ind1], arr[ind2] = arr[ind2], arr[ind1]

def bitonic_merge(arr: list[int], low: int, length: int, direction: int) -> None:
    if length > 1:
        middle=int(length/2)
        for i in range(low, low+middle):
            compare_and_swap(arr, i, i+middle, direction)
        bitonic_merge(arr, low, middle, direction)
        bitonic_merge(arr, low+middle,middle,direction)


def bitonic_sort(arr: list[int], low: int, length: int, direction: int) -> None:
    if length > 1:
        middle=int(length/2)
        bitonic_sort(arr, low, middle, 1)
        bitonic_sort(arr, low+middle,middle,0)
        bitonic_merge(arr, low, length, direction)