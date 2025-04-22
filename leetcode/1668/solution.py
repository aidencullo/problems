class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def check(i):
            total = 0
            for j in range(i, len(sequence)):
                if word[(j - i) % len(word)] != sequence[j]:
                    return total
                total += 1
            return total

        n = len(sequence)
        m = len(word)
        repeating = 0
        for i in range(n):
            repeating = max(check(i), repeating)
        return repeating // len(word)