class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(n):
            digits = num_to_digits(n)
            if len(digits) % 2 == 1:
                return False
            return (sum(digits[:len(digits) // 2]) ==
                    sum(digits[len(digits) // 2:]))

        def num_to_digits(n):
            digits = []
            while n:
                digits.append(n % 10)
                n //= 10
            return digits

        return sum(
            1
            for i in range(low, high + 1)
            if isSymmetric(i)
        )
