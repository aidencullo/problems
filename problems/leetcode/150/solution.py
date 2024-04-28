import math
import operator
from typing import Optional, List, Tuple

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for symbol in tokens:
            try:
                number = int(symbol)
            except ValueError:
                y = stack.pop()
                x = stack.pop()
                stack.append(operate(x, y, symbol))
            else:
                stack.append(int(symbol))
        return stack.pop()

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int( x / y),
}
    
def operate(x, y, op):
    return operators[op](x, y)
