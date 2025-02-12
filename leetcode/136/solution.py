from functools import reduce
import operator

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = set()
        for el in nums:
            if el in seen:
                seen.remove(el)
            else:
                seen.add(el)
        return list(seen)[0]
