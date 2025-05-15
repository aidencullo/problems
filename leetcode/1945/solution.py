class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def convert(s):
            total = 0
            for c in s:
                integer = ord(c) - 96
                total *= 10 if integer < 10 else 100
                total += integer
            return total


        def transform(x):
            sum_of_digits = 0
            while x:
                sum_of_digits += x % 10
                x //= 10
            return sum_of_digits

        s = convert(s)
        for i in range(k):
            s = transform(s)
        return s