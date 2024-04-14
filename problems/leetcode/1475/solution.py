# monotonous stack

# time complexity: O(n)
# space complexity: O(n)


from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = []
        for price in prices[::-1]:
            while stack and stack[-1] > price:
                stack.pop()
            if stack:
                res.append(price - stack[-1])
            else:
                res.append(price)
            stack.append(price)
        return res[::-1]
