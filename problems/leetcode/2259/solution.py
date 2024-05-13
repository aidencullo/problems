class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        digit_count = number.count(digit)
        for i, el in enumerate(number):
            if el == digit and digit_count == 1:
                return number[:i] + number[i + 1:]
            if el == digit and el < number[i + 1]:
                return number[:i] + number[i + 1:]
            if el == digit:
                digit_count -= 1
