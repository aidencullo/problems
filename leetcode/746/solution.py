class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        a = b = c = 0
        for cost in costs + [0]:
            c = cost + min(a, b)
            a = b
            b = c
        return c