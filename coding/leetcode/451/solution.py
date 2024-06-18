from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = Counter(s)
        letters = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        return ''.join(letter * count for letter, count in letters)
