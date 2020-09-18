# Time complexity: O(√N)
# Space complexity: O(1)

import math


def jump_search(arr, x):
    length = len(arr)
    step = math.floor(math.sqrt(length))
    previous = 0

    while arr[min(step, length)-1] < x:
        previous = step
        step += math.floor(math.sqrt(length))

        if previous >= length:
            return -1

    while arr[previous] < x:
        previous += 1

        if previous == min(step, length):
            return -1

    if arr[previous] == x:
        return previous

    return -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print(jump_search(arr, -1) == -1)
print(jump_search(arr, 0) == 0)
print(jump_search(arr, 34) == 9)
print(jump_search(arr, 78) == -1)
print(jump_search(arr, 89) == 11)
print(jump_search(arr, 610) == 15)
print(jump_search(arr, 800) == -1)
