class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = float('inf')
        max_price = float('-inf')
        for i, price in enumerate(prices):
            if price < min_price:
                min_price = price
                max_price = float('-inf')
            max_price = max_update(max_price, price)
            profit = max_update(profit, max_price - min_price)
        return profit
    

def min_update(old, new):
    return min(old, new)

def max_update(old, new):
    return max(old, new)