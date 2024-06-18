import heapq


class Solution:
    def fillCups(self, amount: list[int]) -> int:
        heap = [-num for num in amount]
        heapq.heapify(heap)
        cnt = 0
        while heap:
            a = heapq.heappop(heap)
            if a == 0:
                break
            if heap:
                b = heapq.heappop(heap)
                heapq.heappush(heap, b + 1)
            heapq.heappush(heap, a + 1)
            cnt += 1
        return cnt
