class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeros = arr.count(0)
        n = len(arr)
        l, r = n - 1, n - 1 + zeros
        while l < r:
            if arr[l] == 0:
                if r < n:
                    arr[r] = 0
                r -= 1
            if r < n:
                arr[r] = arr[l]
            l -= 1
            r -= 1
