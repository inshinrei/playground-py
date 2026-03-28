SUBARRAY_LEN = 3


def countStableSubarrays(capacity: list[int]) -> int:
    count = 0

    for i in range(len(capacity)):
        for j in range(i + SUBARRAY_LEN, len(capacity) + 1):
            if considered_stable(capacity[i:j]):
                count += 1

    return count


def considered_stable(arr: list[int]) -> bool:
    print(arr, sum(arr[1 : len(arr)]))

    if arr[0] != arr[-1]:
        return False

    if arr[0] != sum(arr[1 : len(arr) - 1]):
        return False

    return True


countStableSubarrays([9, 3, 3, 3, 9])
