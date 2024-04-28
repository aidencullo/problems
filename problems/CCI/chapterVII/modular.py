"""
Imagine you are writing code to swap the minimum and maximum element in an integer array
"""

def swap_min_max(arr):
    min_el = float('inf')
    max_el = float('-inf')
    min_i = None
    max_i = None
    for i, el in enumerate(arr):
        if el < min_el:
            min_el = el
            min_i = i
        if el > max_el:
            max_el = el
            max_i = i
    arr[max_i], arr[min_i] = arr[min_i], arr[max_i]
    return arr

assert swap_min_max([1, 2, 3, 4, 5]) == [5, 2, 3, 4, 1]
assert swap_min_max([5, 4, 3, 2, 1]) == [1, 4, 3, 2, 5]
assert swap_min_max([1, 5, 3, 4, 2]) == [5, 1, 3, 4, 2]
