class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        k = n // m
        LPS = self.create_prefix_table(word * (k + 1))
        j = 0
        repeating = 0
        i = 0
        while i < n:
            repeating = max(repeating, j // m)
            if sequence[i] == word[j % m]:
                i += 1
                j += 1
                continue
            elif sequence[i] != word[j % m]:
                if j == 0:
                    i += 1
                    continue
                elif j > 0:
                    j = LPS[j - 1]
                    continue
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