class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            k = (l + r) // 2
            target = k * k
            if target < x:
                l = k + 1
            elif target > x:
                r = k - 1
            else:
                return k
        return r
