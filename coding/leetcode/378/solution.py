class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        import itertools
        combined = itertools.chain(*matrix)
        return sorted(combined)[k-1]
