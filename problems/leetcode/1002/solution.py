from collections import Counter
from functools import reduce

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        counters = []
        for word in words:
            counters.append(Counter(word))
        total_counter = reduce(lambda x, y: x & y, counters)
        return list(total_counter.elements())
