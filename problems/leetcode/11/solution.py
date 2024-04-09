# brute force

# time O(n^2)
# space O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_height = 0
        n = len(height)
        for left in range(n):
            for right in range(left, n):
                max_height = max(max_height, min(height[left], height[right]) * (right - left))
        return max_height            


# sliding window

# time O(n)
# space O(1)
    
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_height = 0
        i = 0
        j = len(height) - 1
        while i < j:
            max_height = max(max_height, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_height
