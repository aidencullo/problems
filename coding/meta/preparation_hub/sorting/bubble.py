def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

assert bubble_sort([3, 2, 1]) == [1, 2, 3]
assert bubble_sort([1, 2, 3]) == [1, 2, 3]
assert bubble_sort([1, 3, 2]) == [1, 2, 3]
assert bubble_sort([3, 1, 2]) == [1, 2, 3]
assert bubble_sort([3]) == [3]
assert bubble_sort([]) == []
assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert bubble_sort([1, 2, 3, 5, 4]) == [1, 2, 3, 4, 5]
assert bubble_sort([5, 3, 4, 2, 4, 5, 1, 0, 5, 4, 3, 2, 1]) == [0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5]
