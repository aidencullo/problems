# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums * 2
        stack = []
        res = []
        for num in nums[::-1]:
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(num)
        return res[::-1][:n]
               
