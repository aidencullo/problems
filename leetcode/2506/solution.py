from collections import defaultdict
from math import comb as combination


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        hash_table = defaultdict(int)
        for word in words:
            hash_table[frozenset(word)] += 1

        return sum(combination(n, 2) for n in hash_table.values())
