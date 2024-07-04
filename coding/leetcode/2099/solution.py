class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        max_subarray = []
        for i in range(k):
            max_subarray.append(heapq.heappop(heap))
        max_subarray = [-x for x in max_subarray]
        hash_map = Counter(max_subarray)
        res = []
        for x in nums:
            if x in hash_map:
                hash_map[x] -= 1
                if hash_map[x] == 0:
                    del hash_map[x]
                res.append(x)                    
        return res
