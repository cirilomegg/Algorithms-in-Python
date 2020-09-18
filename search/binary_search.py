# Time complexity: O(log(N))

import math


def binary_search(arr, n):
    arr_length = len(arr)
    start = 0
    end = arr_length - 1

    if arr_length == 0 or arr[start] > n or arr[end] < n:
        return -1

    while start < end:
        half = math.ceil((end - start) / 2) + start

        if n == arr[half]:
            return half
        elif n < arr[half]:
            end = half - 1
        else:
            start = half + 1

    return -1


arr = [2, 3, 4, 5, 9, 14, 57, 78, 90, 95, 97, 99, 123, 345, 567, 789, 890]
print(binary_search(arr, 100) == -1)
print(binary_search(arr, 57) == 6)
