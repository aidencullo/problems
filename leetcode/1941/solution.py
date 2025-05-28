class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        frequencies = Counter(s)
        frequency_counts = Counter(frequencies.values())
        return len(frequency_counts) == 1