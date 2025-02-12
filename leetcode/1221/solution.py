class Solution:
    def balancedStringSplit(self, s: str) -> int:
        Rs = 0
        cnt = 0
        for c in s:
            if c == 'R':
                Rs += 1
            else:
                Rs -= 1
            if Rs == 0:
                cnt +=1
        return cnt
