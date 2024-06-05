from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        diff = t_count - s_count
        return diff.most_common()[0][0]
