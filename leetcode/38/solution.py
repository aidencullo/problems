# time: O(2^n)
# space: O(2^n)

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.say(self.countAndSay(n-1))

    def say(self, digits: str) -> str:
        result = []
        last_digit = digits[0]
        count = 1
        for digit in digits[1:]:
            if digit == last_digit:
                count += 1
            else:
                result.append(str(count) + last_digit)
                count = 1
                last_digit = digit
        result.append(str(count) + last_digit)
        return ''.join(result)
