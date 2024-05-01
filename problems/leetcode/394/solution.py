class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        string = ''
        for symbol in s:
            if symbol == '[':
                stack.append(num)
                stack.append(string)
                num = 0
                string = ''
            elif symbol == ']':
                string = stack.pop() + stack.pop() * string
            elif symbol.isnumeric():
                num = num * 10 + int(symbol)
            else:
                string += symbol
        return ''.join(stack) + string
