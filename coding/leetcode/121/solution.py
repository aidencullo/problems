class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        stack = prices.pop(0)
        profit = 0
        for price in prices:
            if price < stack:
                stack = price
            else:
                profit = max(profit, price - stack)
        return profit
