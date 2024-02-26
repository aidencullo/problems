from collections import defaultdict

class Solution:

    stairs = defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        if self.stairs[n]:
            return self.stairs[n]
        self.stairs[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.stairs[n]
