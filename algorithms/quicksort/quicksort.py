from typing import List


def quicksort(numbers: list[int]) -> List[int]:
    def sort(numbers: list[int], start, end):
        if end <= start:
            return
        pivot_index = partition(numbers, start, end)
        sort(numbers, start, pivot_index-1)
        sort(numbers, pivot_index+1, end)

    sort(numbers, 0, len(numbers)-1)
    return numbers


def partition(numbers: list[int], start: int, end: int):
    pivot = numbers[start]
    l = start + 1
    r = l - 1
    while l < end + 1:
        if numbers[l] <= pivot:
            r += 1
            swap(numbers, l, r)
        l += 1
    swap(numbers, start, r)
    return r


def swap(items, i, j):
    items[i], items[j] = items[j], items[i]
