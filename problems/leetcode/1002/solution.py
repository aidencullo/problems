from collections import Counter
from functools import reduce

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        last_freq = [float('inf')] * 26
        for word in words:
            word_freq = [0] * 26
            for letter in word:
                word_freq[ord(letter) - ord('a')] += 1
            word_freq = [min(a, b) for a, b in zip(last_freq, word_freq)]
            last_freq = word_freq
        return [chr(i + ord('a')) for i, freq in enumerate(last_freq) for _ in range(freq)]
