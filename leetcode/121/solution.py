class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i, price in enumerate(prices):
            for later_price in prices[i + 1:]:
                profit = max(profit, later_price - price)
        return profit