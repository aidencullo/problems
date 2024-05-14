class Solution:
    def minimizedStringLength(self, s: str) -> int:
        stack = []
        for letter in s:
            while stack and stack[-1] == letter:
                stack.pop()
            stack.append(letter)
        return len(stack)

