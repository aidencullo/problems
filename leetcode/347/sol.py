
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_sorted = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        return [key for key, value in freq_sorted[:k]]