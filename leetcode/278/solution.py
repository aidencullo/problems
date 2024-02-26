# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# 1 <= bad <= n <= 231 - 1

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return firstBadVersionRange(1, n)

def firstBadVersionRange(lower: int, upper: int) -> int:
    if lower == upper:
        return lower
    k = (upper + lower) // 2
    if isBadVersion(k):
        return firstBadVersionRange(lower, k)
    else:
        return firstBadVersionRange(k + 1, upper)

def isBadVersion(version: int) -> bool:
    return version > 3
