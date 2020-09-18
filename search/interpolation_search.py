# Time complexity: O (log log n)) for uniformily distributed array. Worst case: O(n).


def interpolation_search(arr, x):
    length = len(arr)

    if length == 0:
        return -1

    lo = 0
    hi = length-1

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        pos = int(lo + ((x - arr[lo]) * (hi-lo) / (arr[hi] - arr[lo])))

        if arr[pos] == x:
            return pos
        elif x > arr[pos]:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 30, 35, 45, 67, 78, 89, 93, 95, 100, 120]
print(interpolation_search(arr, 89) == 14)
