class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        return sorted([x for row in matrix for x in row])[k-1]
