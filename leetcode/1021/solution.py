class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        height = 0
        res = ""
        for c in s:
            if c == "(" and height == 0:
                height += 1
                continue
            if c == "(":
                height += 1
            if c == ")":
                height -= 1
            if height > 0:
                res += c
        return res