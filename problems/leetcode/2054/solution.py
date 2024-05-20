from collections import defaultdict
import heapq

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        last_time = max([end for start, end, value in events])
        events.sort(key=lambda x: x[1])
        end_times = defaultdict(list)
        for event in events:
            end_times[event[1]].append([event[0], event[2]])
        dp = [[] for i in range(last_time + 1)]
        for end in range(1, len(dp)):
            dp[end] = dp[end - 1][:]
            for start, value in end_times[end]:
                heap = dp[start - 1][:]
                max_item = value
                if len(heap) == 2:
                    min_item = heapq.heappop(heap)
                    max_item = max(max_item, min_item)
                heapq.heappush(heap, max_item)
                dp[end] = max(dp[end], heap, key=lambda x: sum(x))
        return sum(dp[-1])
