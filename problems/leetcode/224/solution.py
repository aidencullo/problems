from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: List[str]) -> int:
            stack = []
            op = '+'
            num = 0
            while s:
                symbol = s.pop(0)
                if symbol.isdigit():
                    num = num * 10 + int(symbol)
                elif symbol in '/+*-':
                    if op == '/':
                        stack.append(math.trunc(stack.pop() / num))
                    if op == '*':
                        stack.append(stack.pop() * num)
                    if op == '-':
                        stack.append(-num)
                    if op == '+':
                        stack.append(num)
                    num = 0
                    op = symbol
                elif symbol in '()':
                    if symbol == '(':
                        num = helper(s)
                    if symbol == ')':
                        if op == '/':
                            stack.append(math.trunc(stack.pop() / num))
                        if op == '*':
                            stack.append(stack.pop() * num)
                        if op == '-':
                            stack.append(-num)
                        if op == '+':
                            stack.append(num)                        
                        return sum(stack)
            return sum(stack)
        return helper([*list(s), '+'])
