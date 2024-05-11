class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        else:
            if n < 0:
                return (1 / x) * self.myPow(x, n + 1)
            if n > 0:
                return x * self.myPow(x, n - 1)


"""
idea: based on parity of exp, we can square our running res

ex: myPow(2, 8)
myPow(2, 8)
myPow(2, 4) * myPow(2, 4)
myPow(2, 4) * ...
myPow(2, 2) * myPow(2, 2) * ...
myPow(2, 2) * * ...
myPow(2, 1) * myPow(2, 1) * * ...
"""
