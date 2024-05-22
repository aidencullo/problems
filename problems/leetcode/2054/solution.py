class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        max_two = max(events, key=lambda x: x[2])[2]
        for i in range(len(events)):
            for j in range(i + 1, len(events)):
                start1, end1, value1 = events[i]
                start2, end2, value2 = events[j]
                if start1 > end2 or start2 > end1:
                    max_two = max(max_two, value1 + value2)
        return max_two
