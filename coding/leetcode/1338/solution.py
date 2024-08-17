from collections import Counter

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counter = Counter(arr)
        freqs = sorted(list(counter.items()), key=lambda x: x[1], reverse=True)
        cnt = 0
        for index, (val, freq) in enumerate(freqs):
            cnt += freq
            if cnt >= len(arr) // 2:
                return index + 1
