class Solution:
    def calPoints(self, operations: list[str]) -> int:
        def is_int_str(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            if op == 'C':
                stack.pop()
            if op == 'D':
                stack.append(stack[-1] * 2)
            if is_int_str(op):
                stack.append(int(op))
        return sum(stack)
