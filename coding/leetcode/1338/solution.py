from collections import Counter

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counter = Counter(arr)
        freqs = sorted(list(counter.items()), key=lambda x: x[1], reverse=True)
        res = set()
        cnt = 0
        for val, freq in freqs:
            res.add(val)
            cnt += freq
            if cnt >= len(arr) // 2:
                break
        return len(res)
