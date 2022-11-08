import sys

class Solution:

    hash_map={}
    def __init__(self):
        self.hash_map={}
        
    def coinChange(self, coins: list[int], amount: int) -> int:
        # base case
        if amount == 0:
            return 0
        m = sys.maxsize
        for x in coins:
            # check if we can substract coin value
            if amount >= x:
                if amount - x in self.hash_map:
                    result = self.hash_map[amount - x]
                else:                    
                    result = self.coinChange(coins, amount - x)
                if result != -1:
                    result += 1
                    m = min(m, result)
        # check if valid grouping of coins was found
        if sys.maxsize == m:
            self.hash_map[amount] = -1
            return -1
        else:
            self.hash_map[amount] = m
            return m
