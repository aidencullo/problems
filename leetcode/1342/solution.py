import math

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return str(bin(num)).count('1') + int(math.log(num, 2)) if num else 0
