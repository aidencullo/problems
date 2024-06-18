from operator import itemgetter


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:

        def search(arr, target):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        
        events.sort(key=itemgetter(1))
        ends = [end for _, end, _ in events]
        vals = [val for _, _, val in events]
        dp = [max(vals[:i + 1]) for i in range(len(events))]
        max_val = 0
        for start, end, val in events:
            start_index = search(ends, start - 1)
            if start_index == -1:
                last_val = 0
            else:
                last_val = dp[start_index]
            max_val = max(last_val + val, max_val)
        return max_val
