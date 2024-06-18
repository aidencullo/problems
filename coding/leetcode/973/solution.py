import math
from typing import Optional, List, Tuple


# O(nlogn) time O(n) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x):
            return math.sqrt(x[0]**2 + x[1]**2)
        points.sort(key=lambda x: dist(x))
        return points[:k]
