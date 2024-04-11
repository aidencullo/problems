# time: O(n)
# space: O(n)

from typing import List
import re
import math

class Solution:
    def calculate(self, expr: str) -> int:
        def helper(expr: List[str]):
            stack = []
            op = '+'
            num = 0
            for symbol in expr + ['+']:
                if symbol.isdigit():
                    num = num * 10 + int(symbol)
                else:
                    if op == '*':
                        stack.append(stack.pop() * num)
                    if op == '/':
                        stack.append(math.trunc(stack.pop() / num))
                    if op == '+':
                        stack.append(num)
                    if op == '-':
                        stack.append(-num)
                    num = 0
                    op = symbol
            return sum(stack)

        expr = self.santitize_input(expr)
        return helper(expr)

    def santitize_input(self, expr):
        expr = re.split(r'(\D)', expr)
        return [e for e in expr if e != ' ' and e]

