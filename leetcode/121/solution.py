class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = float('inf')
        for i, price in enumerate(prices):
            if price < buy:
                buy = price
            profit = max(profit, price - buy)
        return profit