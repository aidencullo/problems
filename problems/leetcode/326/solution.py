class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        l, r = 0, n
        while l <= r:
            k = (l + r) // 2
            cube = 3 ** k
            if cube == n:
                return True
            if cube < n:
                l = k + 1
            else:
                r = k - 1
        return False
