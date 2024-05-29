class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        n = len(arr)
        l = k * m
        for i in range(n - l + 1):
            pattern = arr[i: i + m]
            if arr[i: i + l] == pattern * k:
                return True
        return False
