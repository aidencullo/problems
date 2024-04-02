# Type: Two Pointers
# Description: Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water. Notice that you may not slant the container.
# Leetcode: https://leetcode.com/problems/container-with-most-water/

# 11. Container With Most Water



# Solution 1: Two Pointers
# time complexity: O(n)
# space complexity: O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        max_height = float('-inf')
        while left_ptr < right_ptr:
            max_height = max(max_height, (right_ptr-left_ptr) * min(height[left_ptr], height[right_ptr]))
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        return max_height


   
# Solution 2: Brute Force
# time complexity: O(n^2)
# space complexity: O(1)


# from typing import List

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_height = float('-inf')
#         for i, h1 in enumerate(height):
#             for j, h2 in enumerate(height[i+1:]):
#                 max_height = max(max_height, min(h2, h1) * (j+1))
#         return max_height
