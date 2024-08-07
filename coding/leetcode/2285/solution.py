from collections import Counter

class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        degree = Counter()
        degree.update({x:0 for x in range(n)})
        degree.update(node for road in roads for node in road)
        return sum((i + 1) * freq for i, freq in enumerate(sorted(degree.values())))
