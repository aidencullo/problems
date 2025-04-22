class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        repeating = 0
        for i in range(n + 1):
            current = i * word
            if current in sequence:
                repeating = i
        return repeating 