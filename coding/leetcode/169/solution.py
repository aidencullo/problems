"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# ## Solution 1
# """
# actually think this sol is overkill, i thought it was most commonn element, not maj
# """
# # from typing import List

# from collections import Counter

# # O(n) time and space
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return Counter(nums).most_common()[0][0]






## Solution 2
"""
are there only two elements?
"""
from typing import List

from collections import Counter

# # O(n) time and O(1) space
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = 1
#         maj = None
#         for num in nums:
#             if maj is None:
#                 maj = num
#                 count = 1
#             elif maj == num:
#                 count += 1
#             elif maj != num and count == 1:
#                 count = 1
#                 maj = num
#             else:
#                 count -= 1
#         return maj


# ## Solution 3
# """
# still very slow
# """
# from typing import List

# # O(n) time and O(1) space
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = 0
#         maj = None
#         for num in nums:
#             if not count:
#                 maj = num
#                 count = 1
#             elif maj != num:
#                 count -= 1
#             else:
#                 count += 1
#         return maj


## Solution 4
from typing import List

# O(nlogn) time and O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
