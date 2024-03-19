# Solution for the problem Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# O(nlogn) time and O(n) space

"""

Given a collection of intervals, merge all overlapping intervals.

Example:
    
        Input: [[1,3],[2,6],[8,10],[15,18]]
    
        Output: [[1,6],[8,10],[15,18]]
    
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals.pop(0)]
        for start, end in intervals:
            if start <= res[-1][-1]:
                res[-1][-1] = max(end, res[-1][-1])
            else:
                res.append([start, end])
        return res
