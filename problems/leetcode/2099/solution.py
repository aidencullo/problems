import heapq


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        new_heap = heapq.nsmallest(k, heap)
        new_heap.sort(key=lambda x: x[1])
        return [-num for num, _ in new_heap]
