class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        i = n - 1
        digit = digits[i]
        while True:
            if i == -1:
                digits = [0] + digits
                i = 0
                break
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                break
        digits[i] += 1
        return digits
