class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        dp = [0, 0]
        for cost in costs + [0]:
            dp.append(cost + min(dp[-2], dp[-1]))
        return dp[-1]