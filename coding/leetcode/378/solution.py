import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[i].pop(0), i) for i in range(n)]
        heapq.heapify(heap)
        for _ in range(k):
            val, i = heapq.heappop(heap)
            if matrix[i]:
                heapq.heappush(heap, (matrix[i].pop(0), i))
        return val
