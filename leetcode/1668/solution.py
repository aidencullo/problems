class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        LPS = self.create_prefix_table(word)
        n = len(sequence)
        m = len(word)
        j = 0
        repeating = 0
        for i in range(n):
            if sequence[i] == word[j % m]:
                i += 1
                j += 1
            else:
                j = LPS[(j - 1) % m]
            repeating = max(repeating, j // m)
        return repeating

    def create_prefix_table(self, pattern: str) -> list:
        m = len(pattern)
        prefix = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                prefix[i] = j
        return prefix
