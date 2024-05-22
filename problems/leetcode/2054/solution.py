from operator import itemgetter


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort(key=itemgetter(1))
        ends = [end for _, end, _ in events]
        dp = []
        for start, end, val in events:
            start_index = search(ends, start - 1)
            if start_index == -1:
        return dp[-1]
