import heapq


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        heap = [(row.count(1), i) for i, row in enumerate(mat)]
        heapq.heapify(heap)
        return [idx for soldiers, idx in heapq.nsmallest(k, heap)]
