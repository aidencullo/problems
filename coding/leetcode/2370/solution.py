class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        longest = {i: 0 for i in range(26)}
        for i, c in enumerate(s):
            c_longest = 0
            z = ord(c) - ord('a')
            for j in range(-k, k + 1):
                if z + j >= 0 and z + j < 26:
                    c_longest = max(c_longest, longest[z + j])
            longest[ord(c) - ord('a')] = c_longest + 1
        return max(longest.values())
