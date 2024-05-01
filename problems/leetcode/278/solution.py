# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            k = l + (r - l) // 2
            is_bad = isBadVersion(k)
            if is_bad:
                r = k - 1
            else:
                l = k + 1
        return l
