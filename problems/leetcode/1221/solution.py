class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        opposite = {'R': 'L', 'L': 'R'}
        cnt = 0
        for c in s:
            if stack and stack[-1] == opposite[c]:
                stack.pop()
            else:
                stack.append(c)
            if not stack:
                cnt +=1
        return cnt
