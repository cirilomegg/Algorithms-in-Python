# Time complexity: O(N)
# Space complexity: O(1)


def linear_search(arr, x):
    length = len(arr)

    for i in range(0, length):
        if arr[i] == x:
            return i

    return -1


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print(linear_search(arr, -1) == -1)
print(linear_search(arr, 0) == 0)
print(linear_search(arr, 34) == 9)
print(linear_search(arr, 78) == -1)
print(linear_search(arr, 89) == 11)
print(linear_search(arr, 610) == 15)
print(linear_search(arr, 800) == -1)
