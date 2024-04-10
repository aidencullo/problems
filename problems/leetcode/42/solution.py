# monotonic stack

# time O(n)
# space O(n)

from typing import List

class Solution:

    def trap(self, heights: List[int]) -> int:
        max_index = heights.index(max(heights))
        return self.helper(heights[:max_index+1]) + self.helper(heights[max_index:][::-1])

    def helper(self, heights: List[int]) -> int:
        stack = []
        for i, height in enumerate(heights):
            if not stack or heights[stack[-1]] <= height:
                stack.append(i)
        return self.collect_water(stack, heights)

    def collect_water(self, stack, heights):
        water = 0
        for i in range(len(stack)-1):
            left = stack[i]
            right = stack[i+1]
            left_bar = heights[left]
            right_bar = heights[right]
            water += (right - left - 1) * min(left_bar, right_bar)
            water -= sum(heights[left+1:right])
        return water







# dynamic programming

# time O(n)
# space O(n)

from typing import List

class Solution:

    def trap(self, heights: List[int]) -> int:
        left = [0] * len(heights)
        max_left = 0
        for i in range(len(heights)):
            left[i] = max_left
            max_left = max(max_left, heights[i])

        right = [0] * len(heights)
        max_right = 0
        for i in range(len(heights)-1, -1, -1):
            right[i] = max_right
            max_right = max(max_right, heights[i])

        water = 0
        for i in range(len(heights)):
            water += max(min(left[i], right[i]) - heights[i], 0)

        return water
