import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = sorted(nums)[-k:]
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
