class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stack = []
        for letter in s:
            if letter == '(':
                if stack:
                    result.append(letter)
                stack.append(letter)
            else:
                if len(stack) > 1:
                    result.append(letter)
                stack.pop()                    
        return ''.join(result)
