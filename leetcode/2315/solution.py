class Solution:
    def countAsterisks(self, s: str) -> int:
        on = True
        total = 0
        for c in s:
            if on and c == "*":
                total += 1
            if c == "|":
                on = not on
        return total