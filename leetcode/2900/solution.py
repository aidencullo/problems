class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        res = []
        for i, __ in enumerate(words):
            if i == 0:
                res.append(words[i])
                continue
            if groups[i] != groups[i-1]:
                res.append(words[i])
                continue
        return res
