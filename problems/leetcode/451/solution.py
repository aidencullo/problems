from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = Counter(s)
        s = list(s)
        s.sort(key=lambda x: (hash_map[x], x), reverse=True)
        return ''.join(s)
