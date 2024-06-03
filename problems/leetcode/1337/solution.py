class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        soldiers = [(sum(row), i) for i, row in enumerate(mat)]
        soldiers.sort()
        return [i for s, i in soldiers[:k]]
