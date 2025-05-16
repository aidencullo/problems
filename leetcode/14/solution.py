from itertools import zip_longest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        if len(strs) == 1:
            return shortest
        if shortest == "":
            return ""
        prefix = ""
        for i in range(len(shortest)):
            letter = shortest[i]
            for word in strs:
                if letter != word[i]:
                    return prefix
            prefix += letter
        return prefix
