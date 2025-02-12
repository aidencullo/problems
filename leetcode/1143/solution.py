# time: O(n*m)
# space: O(n*m)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        d = [[0] * (n+1) for _ in range(m+1)]
        for j in range(1, m+1):
            for i in range(1, n+1):
                if text2[j-1] == text1[i-1]:
                    d[j][i] = d[j-1][i-1] + 1
                else:
                    d[j][i] = max(d[j][i-1], d[j-1][i])
        return d[-1][-1]
