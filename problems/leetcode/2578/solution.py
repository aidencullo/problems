# time: O(logn)
# space: O(logn)

class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        digits.sort(reverse=True)
        left = ""
        right = ""
        while digits:
            left += str(digits.pop())
            if digits:
                right += str(digits.pop())
        return int(left) + int(right)
