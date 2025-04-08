class Solution:

    def __init__(self):
        self.mem = {}

    def climbStairs(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        self.mem[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.mem[n]
