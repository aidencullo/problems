"""
Imagine you are writing code to swap the minimum and maximum element in an integer array
"""

def swap_min_max(arr):
    min_i =  get_min_index(arr)
    max_i = get_max_index(arr)
    arr[max_i], arr[min_i] = arr[min_i], arr[max_i]
    return arr


def get_min_index(arr):
    return arr.index(min(arr))


def get_max_index(arr):
    return arr.index(max(arr))


assert swap_min_max([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]
assert swap_min_max([5, 4, 3, 2, 1]) == [1, 4, 3, 2, 5]
assert swap_min_max([1, 5, 3, 4, 2]) == [5, 1, 3, 4, 2]
