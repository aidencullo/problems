class Solution:
    def maxDepth(self, s: str) -> int:
        max_stack = 0
        cur_stack = 0
        for symbol in s:
            if symbol == '(':
                cur_stack += 1
                max_stack = max(max_stack, cur_stack)
            if symbol == ')':
                cur_stack -= 1
        return max_stack
