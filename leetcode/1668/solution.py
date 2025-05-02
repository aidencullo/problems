class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        repeating = 0
        for i in range(n + 1):
            if i * word in sequence:
                repeating = i
        return repeating