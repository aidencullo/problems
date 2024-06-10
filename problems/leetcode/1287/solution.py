from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        cnt = 0
        last = -1
        for el in arr:
            if el == last:
                cnt += 1
            else:
                last = el
                cnt = 1
            if cnt > n / 4:
                return el
