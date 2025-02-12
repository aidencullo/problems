class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_unique = set(allowed)
        count = len(words)
        for word in words:
            for char in word:
                if char not in allowed_unique:
                    count -= 1
                    break
        return count
