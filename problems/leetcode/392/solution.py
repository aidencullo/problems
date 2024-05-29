class Solution:
    def isSubsequence(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)
        dp = [{} for _ in range(m + 1)]
        for j in range(m - 1, -1, -1):
            dp[j] = dp[j + 1].copy()
            dp[j][word2[j]] = j
        cur_dict = dp[0]
        dp = dp[1:]
        for i, el in enumerate(word1):
            if not el in cur_dict:
                return False
            cur_dict = dp[cur_dict[el]]
        return True
