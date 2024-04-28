def bubble_sort(arr):
    for __ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

assert bubble_sort([3, 2, 1]) == [1, 2, 3]
assert bubble_sort([1, 2, 3]) == [1, 2, 3]
assert bubble_sort([1, 3, 2]) == [1, 2, 3]
assert bubble_sort([3, 1, 2]) == [1, 2, 3]
assert bubble_sort([3]) == [3]
assert bubble_sort([]) == []

