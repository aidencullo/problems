class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def countBits(n: int) -> list[int]:
            return bin(n).count('1')
        return sorted(arr, key=lambda x: (countBits(x), x))
