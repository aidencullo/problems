class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        stack = []
        for letter in s:

            if letter == '(' and not stack:
                stack.append(letter)
                continue
            if letter == ')' and len(stack) == 1:
                stack.pop()
                continue

            result += letter
            if letter == '(':
                stack.append(letter)
            else:
                stack.pop()                    

        return result
