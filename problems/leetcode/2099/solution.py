# time complexity: O(n + k * log(n) + k * log(k))
# time complexity: O(n * log(n))
# space complexity: O(n)


import heapq


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        heap = [(-num, i) for i, num in enumerate(nums)] # O(n)
        heapq.heapify(heap) # O(n)
        new_heap = heapq.nsmallest(k, heap) # O(k * log(n))
        new_heap.sort(key=lambda x: x[1]) # O(k * log(k))
        return [-num for num, _ in new_heap] # O(k)
