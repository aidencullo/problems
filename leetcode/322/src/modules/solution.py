import sys

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # base case
        if amount == 0:
            return 0
        m = sys.maxsize
        for x in coins:
            if amount >= x:
                result = 1 + self.coinChange(coins, amount - x)
                if result != 0:
                    m = min(m, result)
        if sys.maxsize == m:
            return -1
        else:
            return m
