class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                if x == y:
                    result += abs(i - j)
        return result
