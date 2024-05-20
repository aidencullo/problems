class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def minCostClimbingStairsHelper(cost: list[int]) -> int:
            if not cost:
                return 0
            return cost[0] + min(minCostClimbingStairsHelper(cost[1:]), minCostClimbingStairsHelper(cost[2:]))
        return min(minCostClimbingStairsHelper(cost), minCostClimbingStairsHelper(cost[1:]))
