class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeros = sum((1 if x == 0 else 0 for x in arr))
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
