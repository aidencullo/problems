class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def countBits(n: int) -> list[int]:
            result = [0] * (n + 1)
            for i in range(n + 1):
                result[i] = result[i >> 1] + (i & 1)
            return result[-1]
        return sorted(arr, key=lambda x: (countBits(x), x))
