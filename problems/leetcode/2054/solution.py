from collections import defaultdict
import heapq

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        last_time = max([end for start, end, value in events])
        events.sort(key=lambda x: x[1])
        end_times = defaultdict(list)
        for start, end, value in events:
            end_times[end].append([start, value])
        dp = [0] * (last_time + 1)
        max_two = 0
        for end in range(1, len(dp)):
            dp[end] = dp[end - 1]
            for start, value in end_times[end]:
                max_two = max(max_two, value + dp[start - 1])
                dp[end] = max(value, dp[end])
        return max_two
