class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s: str):
            stack = []
            for letter in s:
                if letter == "#" and not stack:
                    continue
                if letter == "#":
                    stack.pop()
                else:
                    stack.append(letter)
            return "".join(stack)
        s_backspace =  backspace(s)
        t_backspace =  backspace(t)
        return s_backspace == t_backspace
