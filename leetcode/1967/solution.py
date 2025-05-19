class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        strs = 0

        for pattern in patterns:
            if pattern in word:
                strs += 1
        return strs