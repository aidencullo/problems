from typing import List
import re
import math

class Solution:
    def calculate(self, expr: str) -> int:
        def helper(expr: List[str]):
            stack = []
            stack.append(int(expr.pop(0)))
            for symbol in expr:
                if symbol.isdigit():
                    num = int(symbol)
                    if op == '*':
                        stack.append(stack.pop() * num)
                    if op == '/':
                        stack.append(math.trunc(stack.pop() / num))
                    if op == '+':
                        stack.append(num)
                    if op == '-':
                        stack.append(-num)
                else:
                    op = symbol
            return sum(stack)
        expr = re.sub(' ', '', expr)
        expr = re.split(r'(\D)', expr)
        expr = [e for e in expr if e]
        return helper(expr)
