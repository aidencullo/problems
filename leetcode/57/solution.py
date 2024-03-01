## Solution 1
from typing import List

from utils import combine, intersect


# O(n) time and space
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        running = None
        ran = False
        results = []

        for interval in intervals:
            if intersect(newInterval, interval):
                running = combine(newInterval, interval, running)
                ran = True
            else:
                if running:
                    results.append(running)
                    running = None
                else:
                    if newInterval < interval and not ran:
                        ran = True
                        results.append(newInterval)
                results.append(interval)
        if running:
            results.append(running)            
        if not ran:
            results.append(newInterval)
        return results
