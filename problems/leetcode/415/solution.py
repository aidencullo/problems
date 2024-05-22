from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        res = []
        for x, y in zip_longest(num1, num2, fillvalue='0'):
            a = int(x)
            b = int(y)
            c = a + b + carry
            res.append(str(c % 10))
            carry = c // 10
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
