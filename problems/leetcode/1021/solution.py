class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        stack = []
        on = False
        for letter in s:
            if letter == '(':
                if stack:
                   result += letter
                stack.append(letter)
            else:
                if len(stack) > 1:
                   result += letter
                stack.pop()                    
        return result
