from typing import Callable

ComparisonFunction = Callable[[int, int], int]

class Solution:

    def canSortArray(self, nums: list[int]) -> bool:
        from functools import cmp_to_key
        def compare_people(x, y):
            if x.bit_count() != y.bit_count():
                return 1
            return y - x
        def bubble_sort(arr: list[int], compare: ComparisonFunction) -> list[int]:
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if compare(arr[j], arr[j + 1]) > 0:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr
        nums = bubble_sort(nums, compare_people)
        print("Sorted array:", nums)
        return nums == sorted(nums)
