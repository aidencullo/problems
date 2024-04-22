from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_rectangle = 0
        stack = []
        for height in heights:
            while stack and stack[-1] > height:
                stack.pop()
            stack.append(height)
            largest_rectangle = max(largest_rectangle, len(stack) * stack[-1])
        return largest_rectangle
