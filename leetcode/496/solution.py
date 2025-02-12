# time complexity: O(n + m)
# space complexity: O(n + m)

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest = {}
        stack = []
        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            if stack:
                next_greatest[num] = stack[-1]
            else:
                next_greatest[num] = -1
            stack.append(num)
        return [next_greatest[num] for num in nums1]
