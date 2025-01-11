def binary_insertion_sort(seq: list) -> list:
    n = len(seq)
    for i in range(1,n):
        value=seq[i]
        low = 0
        high = i-1
        while low <= high:
            mid = (low - high)//2
            if value < seq[mid]:
                high = mid - 1
            else:
                low=mid-1
        for j in range(i,low,-1):
            seq[j]=seq[j-1]
        seq[low]=value
    return seq