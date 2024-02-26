## Solution 2

# from functools import cache

# # O(n) time complexity O(n) space
# class Solution:
#     @cache
#     def climbStairs(self, n: int) -> int:
#         if n < 3:
#             return n
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)







## Solution 2
# 32 ms
# O(n) time complexity O(1) space
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         a = 0
#         b = 1
#         c = 0
#         for _ in range(n):
#             c = a + b
#             a = b
#             b = c
#         return c







## Solution 3
# 36 ms
# O(n) time complexity O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return b
