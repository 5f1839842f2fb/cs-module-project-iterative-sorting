import math

def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    val = math.floor(len(arr)/2)
    # Your code here
    workingarr = arr
    while len(workingarr) > 0:
        i = math.floor(len(workingarr)/2)
        if workingarr[i] == target:
            return val
        if arr[i] < target:
            val += 1
            workingarr = workingarr[i + 1:]
        else:  # if arr[i] > target:
            workingarr = workingarr[0:i]

    return -1  # not found
