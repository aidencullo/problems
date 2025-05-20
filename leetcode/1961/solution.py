class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        while s: # n
            if not words:
                return False
            current = words.pop(0) # m, m^2 total
            if s.find(current) != 0: # k (1...n), n^2 total
                return False
            s = s[len(current):] # k (n...1), n^2 time/space
        return True