import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def kth(nums: List[int], k: int, start: int, end: int) -> int:
            if end <= start:
                return nums[k]
            pivot_index = partition(nums, start, end)
            pivot = nums[pivot_index]
            if pivot_index < k:
                return kth(nums, k, pivot_index+1, end)
            if pivot_index > k:
                return kth(nums, k, start, pivot_index-1)
            return pivot

        return kth(nums, len(nums) - k, 0, len(nums)-1)


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
