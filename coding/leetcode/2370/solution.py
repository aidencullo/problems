class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        def get_longest(c, k):
            new_pos = ord(c) - ord('a') + k
            if new_pos >= 26 or new_pos < 0:
                return 0
            return self.longest[new_pos]
        n = len(s)
        total = 0
        self.longest = {i: 0 for i in range(26)}
        for i, c in enumerate(s):
            c_longest = 0
            for j in range(k + 1):
                c_longest = max(c_longest, get_longest(c, j))
                c_longest = max(c_longest, get_longest(c, -j))
            self.longest[ord(c) - ord('a')] = c_longest + 1
        return max(self.longest.values())
