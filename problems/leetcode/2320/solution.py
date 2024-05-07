from typing import List

class Solution:
    def countHousePlacements(self, n: int) -> int:
        def helper(n: int, h: int) -> int:
            if n == 0:
                if 0 <= h and h <= 2:
                    return 1
                return 0
            return helper(n - 1, h) + 2 * helper(n - 1, h - 1) + helper(n - 1, h - 2)
        return helper(n, n + 1)
        
