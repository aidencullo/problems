class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0
        for letter in s:
            if letter == '(':
                if opened > 0:
                    result.append(letter)
                opened += 1
            else:
                if opened > 1:
                    result.append(letter)
                opened -= 1
        return ''.join(result)
