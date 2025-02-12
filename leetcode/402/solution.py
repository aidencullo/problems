class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        min_stack = []
        for digit in num:
            while min_stack and min_stack[-1] > digit and k > 0:
                min_stack.pop()
                k -= 1
            if digit != '0':
                min_stack.append(digit)
            if digit == '0' and min_stack:
                min_stack.append(digit)
        while min_stack and k > 0:
            min_stack.pop()
            k -= 1
        return ''.join(min_stack) if k == 0 and min_stack else "0"
