from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = Counter(words)
        word_counter = [(-count, word) for word, count in word_counter.items()]
        heapq.heapify(word_counter)
        return [heapq.heappop(word_counter)[1] for _ in range(k)]
