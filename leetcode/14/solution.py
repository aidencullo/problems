from itertools import zip_longest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        prefix = []
        for i in range(len(shortest)):
            letter = shortest[i]
            for word in strs:
                if letter != word[i]:
                    return ''.join(prefix)
            prefix.append(letter)
        return ''.join(prefix)
