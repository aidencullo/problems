class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(-num, i) for i, num in enumerate(nums)]
        heap = heapq.heapify(nums)
        max_subarray = []
        for i in range(k):
            max_subarray.append(heapq.heappop(nums))
        max_subarray.sort(key=lambda x: x[1])
        return [-x for x, y in max_subarray]
