class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed = set(allowed)
        return sum(1 for word in words if all(c in allowed for c in word))
