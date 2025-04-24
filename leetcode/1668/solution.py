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
        for i in range(m):
            if i > 0:
                last = pattern[prefix[i - 1]]
                if pattern[i] == last:
                    prefix[i] = prefix[i - 1] + 1
                else:
                    if prefix[prefix[i - 1]] > 0:
                        prefix[i] = prefix[prefix[i - 1]] - 1
        return prefix
