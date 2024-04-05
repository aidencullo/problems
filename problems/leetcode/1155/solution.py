# time: O(n * target * k)
# space: O(n * target * k)

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        d = [[[0] * (k+1) for __ in range(target+1)] for __ in range(n+1)]
        d[0][0][0] = 1
        for i in range(1, n+1):
            for j in range(1, target+1):
                for l in range(1, k+1):
                    if j >= l:
                        d[i][j][l] = sum(d[i-1][j-l])
        return sum(d[-1][-1]) % (10**9 + 7)
        
