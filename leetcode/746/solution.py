class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def climb(i):
            if i > len(cost):
                return 0
            return min(
                cost[i] + climb(i + 1)
                cost[i] + climb(i + 2)
                )
        return climb(-1)