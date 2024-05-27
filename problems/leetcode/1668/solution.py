class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        m = len(word)
        n = len(sequence)
        max_cnt = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n, m):
                contender = sequence[j: j + m]
                if contender == word:
                    cnt += 1
                else:
                    break
            max_cnt = max(max_cnt, cnt)
        return max_cnt


"""
approach

1. iterate over letters and keep track of some counter/info?
- linear time and constant/linear space?

what is brute force?
1. O(n^2) time O(1) space
a. begin at each letter and count contiguous occurrences of word

how/what can we optimize?
1. second n
2. counter/dict for letters?
3. but then how do we keep track of the order? of the substr
4. hint says contraints are low enough for brute-force approach
"""

