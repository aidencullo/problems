class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        def minCostClimbingStairsHelper(index: int) -> int:
            if index > len(cost) - 1:
                return 0

            if not index in self.mem:
                self.mem[index] = cost[index] + min(
                    minCostClimbingStairsHelper(index + 1),
                    minCostClimbingStairsHelper(index + 2)
                )
            return self.mem[index]

        self.mem = {}
        return min(
            minCostClimbingStairsHelper(0),
            minCostClimbingStairsHelper(1)
        )
