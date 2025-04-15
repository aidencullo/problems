class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        maximum = 0
        for i, start in enumerate(sequence):
            for j, current in enumerate(sequence[i:]):
                if current != word[j % len(word)]:
                    break
                maximum = max(maximum, j + 1)
        return maximum // len(word)