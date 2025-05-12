class Solution:
    def countAsterisks(self, s: str) -> int:
        bars = 0
        total = 0
        for c in s:
            if bars % 2 == 0 and c == "*":
                total += 1
            if c == "|":
                bars += 1
        return total