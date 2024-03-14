import math
import operator
from typing import Optional, List, Tuple

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '/' : lambda x, y: int(x/y),
            '*' : operator.mul,
        }
        for token in tokens:
            if token in ops:
                r = int(stack.pop())
                l = int(stack.pop())
                stack.append(ops[token](l, r))
            else:
                stack.append(token)
        return int(stack.pop())
