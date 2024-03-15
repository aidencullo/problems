# from typing import Optional, List, Tuple

# class Solution:
    
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         def coinChangeHelper(coins: List[int], amount: int) -> int:
#             if amount <= 0:
#                 return amount
#             min_coins = float('inf')
#             for coin in coins:
#                 if amount - coin in self.mem:
#                     sub_change = self.mem[amount - coin]
#                 else:
#                     sub_change = coinChangeHelper(coins, amount - coin)
#                     self.mem[amount - coin] = sub_change
#                 if sub_change >= 0:
#                     min_coins = min(min_coins, sub_change + 1)
#             if min_coins == float('inf'):
#                 return -1
#             return min_coins

#         self.mem = {}
#         return coinChangeHelper(coins, amount)







from typing import Optional, List, Tuple

class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = [amount + 1] * (amount + 1)

        d[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    d[a] = min(d[a], 1 + d[a - c])
        return d[amount] if d[amount] != amount + 1 else -1
