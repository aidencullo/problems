class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_nums1 = m - 1
        index_nums2 = n - 1
        index_merged = m + n - 1
        while index_merged >= 0:
            n1 = float('-inf') if index_nums1 < 0 else  nums1[index_nums1]
            n2 = float('-inf') if index_nums2 < 0 else  nums2[index_nums2]
            if n1 >= n2:
                nums1[index_merged] = nums1[index_nums1]
                index_merged -= 1
                index_nums1 -= 1
            else:
                nums1[index_merged] = nums2[index_nums2]
                index_merged -= 1
                index_nums2 -= 1


"""
- INPUT: two integer lists: nums1, nums2, size m,n
-- sorted in non-decreasing order
-- could be [1,2,2,2,2,2]
- GOAL: sort nums1, and nums2 in-place!

- constraints?
-- size of arrays
-- ranges of inputs
-- empty lists?
-- Null input?
-- not enough space?
-- all zeros?
-- floats?
-- extra memory?
-- nums2 free space?

- ideas
-- pointer on first el of nums1/2
-- move all nums1 to the end of list
-- iterate over nums1/2 concurrently
-- min el (or either if ==) assign smaller
--- 3 pointers:
---- current nums1 el
---- current nusm2 el
---- current position to be filled in output (nums1)

- time complexity?
-- copy els to end - n
-- iterate over nums1/2 - n + m
-- total - n + m
-- space? - constant
-- BCR? can we improve?
--- than n + m -- highly doubt it?
--- can i implement it now? ;)
"""


"""
Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""

"""
size of lists very small
- 10^9 what is that? 1 billion? size of int in C
-- near max C int
-- what does this mean?
-- not double/floats
"""

"""
approach
-- wait let's just do the opposite, fill in nums1 (size m+n) from the back, no need to copy any values
-- problems?
-- space?
--- nums1 <, > nums2?
-- insert max (nums1, nums2)
"""

"""
ex:
1. nums1 = [1,2,3,0,0,0]
2. nums2 = [4,5,6]

nums1 ptr = (index) 2
nums2 ptr = (index) 2
6 >= 3 => yes => ins 6
mv ptr2 to 1
5 >= 3 => yes => ins 5
mv ptr2 to 0
4 >= 3 => yes => ins 5
mv ptr2 to -1
"""
