class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partner = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                if partner[c] != stack.pop():
                    return False
        return not stack
