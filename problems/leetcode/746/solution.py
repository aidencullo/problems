from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        @cache
        def minCostClimbingStairsHelper(index: int) -> int:
            if index > len(cost) - 1:
                return 0
            return cost[index] + min(minCostClimbingStairsHelper(index + 1), minCostClimbingStairsHelper(index + 2))
        return min(minCostClimbingStairsHelper(0), minCostClimbingStairsHelper(1))
