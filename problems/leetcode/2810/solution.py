class Solution:
    def finalString(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter == 'i':
                stack = stack[::-1]
            else:
                stack.append(letter)
        return "".join(stack)
