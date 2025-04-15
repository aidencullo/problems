class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def climb(i):
            if i > len(cost) - 1:
                return 0
            if not i in self.memo:            
                self.memo[i] = min(
                    cost[i] + climb(i + 1),
                    cost[i] + climb(i + 2)
                    )
            return self.memo[i]

        self.memo = {}
        return min(climb(0), climb(1))