class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            hashset = set()
            cnt = 0
            for j in range(i, n):
                char = s[j]
                if char not in hashset:
                    hashset.add(char)
                    if char.lower() in hashset and char.upper() in hashset:
                        cnt -= 1
                    else:
                        cnt += 1
                if cnt == 0 and j - i + 1 > len(res):
                    res = s[i:j + 1]
        return res
