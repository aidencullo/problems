class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        counter = Counter(s)
        return len(Counter(counter.values())) == 1
        