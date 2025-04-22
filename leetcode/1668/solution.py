class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        k = n // m
        repeating = 0
        for i in range(k + 1):
            current = i * word
            if current in sequence:
                repeating = i
        return repeating 