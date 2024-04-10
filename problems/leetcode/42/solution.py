from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        max_height = max(heights)
        max_index = heights.index(max_height)
        heights_reversed = heights[::-1]
        heights_reversed = heights_reversed[:len(heights)-max_index]
        return self.helper(heights[:max_index+1]) + self.helper(heights_reversed)
    def helper(self, heights: List[int]) -> int:
        stack = []
        next_heights = []
        total_water = 0
        n = len(heights)
        for i, height in enumerate(heights[::-1]):
            while stack and stack[-1][1] < height:
                stack.pop()
            if stack:
                next_heights.append(stack[-1][0])
            else:
                next_heights.append(-1)
            stack.append((n - i - 1, height))
        next_heights.reverse()
        i = 0
        water = 0
        while i < n:
            if next_heights[i] == -1:
                break
            water += (next_heights[i] - i - 1) * min(heights[i], heights[next_heights[i]])
            water -= sum(heights[i + 1: next_heights[i]])
            i = next_heights[i]
        return water
