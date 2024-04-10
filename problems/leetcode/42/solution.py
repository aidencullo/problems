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
        left = [heights[0]] * len(heights)
        for i in range(1, len(heights)):
            left[i] = max(left[i-1], heights[i])

        right = [heights[-1]] * len(heights)
        for i in range(len(heights)-2, -1, -1):
            right[i] = max(right[i+1], heights[i])

        return sum(min(left[i], right[i]) - heights[i] for i in range(len(heights)))






# # two pointers

# # time O(n)
# # space O(1)

# from typing import List

# class Solution:

#     def trap(self, heights: List[int]) -> int:
#         max_l = max_r = 0
#         l = 0
#         r = len(heights) - 1
#         water = 0
#         while l <= r:
#             if max_l < max_r:
#                 water += max(max_l - heights[l], 0)
#                 max_l = max(max_l, heights[l])
#                 l += 1
#             else:
#                 water += max(max_r - heights[r], 0)
#                 max_r = max(max_r, heights[r])
#                 r -= 1
#         return water







# # brute force

# # time O(n^2)
# # space O(1)

# from typing import List

# class Solution:

#     def trap(self, heights: List[int]) -> int:
#         water = 0
#         for i in range(len(heights)):
#             max_l = 0
#             max_r = 0
#             for j in range(i+1, len(heights)):
#                 max_r = max(max_r, heights[j])
#             for j in range(i-1, -1, -1):
#                 max_l = max(max_l, heights[j])
#             water += max(0, min(max_l, max_r) - heights[i])
#         return water
