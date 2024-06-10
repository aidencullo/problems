class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        def leftBound(target: int) -> int:
            l, r = 0, len(arr) - 1
            while l <= r:
                k = (l + r) // 2
                if arr[k] < target:
                    l = k + 1
                else:
                    r = k - 1
            return l

        def rightBound(target: int) -> int:
            l, r = 0, len(arr) - 1
            while l <= r:
                k = (l + r) // 2
                if arr[k] <= target:
                    l = k + 1
                else:
                    r = k - 1
            return r

        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[(3*n) // 4]]
        for candidate in candidates:
            l = leftBound(candidate)
            r = rightBound(candidate)
            if r - l + 1 > n // 4:
                return candidate
