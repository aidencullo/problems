from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        total = 0
        seen = defaultdict(int)
        for hour in hours:
            target = (24 - hour) % 24
            if target in seen:
                total += seen[target]
            seen[hour % 24] += 1
        return total
