# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ans = 0
        num = 0
        sign = 1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ans = ans + sign * num
                num = 0
                continue
            if s[i] == '+':
                sign = 1
            if s[i] == '-':
                sign = -1
            if s[i] == '(':
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            if s[i] == ')':
                ans *= stack.pop()
                ans += stack.pop()
            i += 1
        return ans
