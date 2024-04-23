from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        x = Counter(words)
        sorted_counter = sorted(x.items(), key=lambda item:(-item[1], item[0]))
        k_sorted_counter = sorted_counter[:k]
        k_sorted_counter = [word for word, count in k_sorted_counter]
        return k_sorted_counter
