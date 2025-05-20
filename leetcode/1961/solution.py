class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        while s:
            if not words:
                return False
            current = words.pop(0)
            if not s.startswith(current):
                return False
            s = s[len(current):]
        return True