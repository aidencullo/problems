# ## Solution 1
# from typing import List

# from utils import combine, intersect


# # O(n) time and space
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         running = None
#         ran = False
#         results = []

#         for interval in intervals:
#             if intersect(newInterval, interval):
#                 running = combine(newInterval, interval, running)
#                 ran = True
#             else:
#                 if running:
#                     results.append(running)
#                     running = None
#                 else:
#                     if newInterval < interval and not ran:
#                         ran = True
#                         results.append(newInterval)
#                 results.append(interval)
#         if running:
#             results.append(running)            
#         if not ran:
#             results.append(newInterval)
#         return results


## Solution 2
"""
slower but clearer/shorter
"""
from typing import List

from utils import combine, intersect

# O(nlogn) time and O(n) space
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        current = intervals[0]
        results = []
        for interval in intervals[1:]:
            if intersect(current, interval):
                current = combine(current, interval)
            else:
                results.append(current)
                current = interval
        results.append(current)
        return results
