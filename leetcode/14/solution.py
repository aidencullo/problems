class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for chars in zip(*strs):
            letter = chars[0]
            for c in chars:
                if c != letter:
                    return ''.join(prefix)
            prefix.append(letter)
        return ''.join(prefix)
