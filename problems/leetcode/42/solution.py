# time O(n)
# space O(n)

from typing import List

class Solution:

    def trap(self, heights: List[int]) -> int:
        max_index = heights.index(max(heights))
        return self.helper(heights[:max_index+1]) + self.helper(heights[max_index:][::-1])

    def helper(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        for i, height in enumerate(heights):
            if not stack or heights[stack[-1]] <= height:
                stack.append(i)
        water = 0
        for i in range(len(stack)-1):
            left = stack[i]
            right = stack[i+1]
            left_bar = heights[left]
            right_bar = heights[right]
            water += (right - left - 1) * min(left_bar, right_bar)
            water -= sum(heights[left+1:right])
        return water
