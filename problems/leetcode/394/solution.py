class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        numbers = []
        num = 0
        string = ''
        for symbol in s:
            if symbol == '[':
                numbers.append(num)
                num = 0
                stack.append(string)
                string = ''
            if symbol.isnumeric():
                num = num * 10 + int(symbol)
            if symbol.isalpha():
                string += symbol
            if symbol == ']':
                string *= numbers.pop()
                string = stack.pop() + string
        return ''.join(stack) + string
