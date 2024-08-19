import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(heap, (arr[i] / arr[j], arr[i], arr[j]))
        res = 0
        for i in range(k):
            res = heapq.heappop(heap)
        return [res[1], res[2]]
