class Solution:
    def myPow(self, x: float, n: int) -> float:
        def exponentiation(x: float, n: int):
            if n == 0:
                return 1
            if n % 2:
                return x * self.myPow(x*x, (n-1)/2)
            return self.myPow(x*x, n/2)

        if n < 0:
            return exponentiation(1/x, -n)
        return exponentiation(x, n)
