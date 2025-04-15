class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        revenue = 0
        stack = []
        for price in prices:
            while stack and stack[-1] > price:
                stack.pop()
            stack.append(price)
            if len(stack) > 1:
                revenue = max(stack[-1] - stack[0], revenue)

        return revenue