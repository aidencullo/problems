class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            if char in ')]}':
                if len(stack) == 0:
                    return False
                if char != flip(stack.pop()):
                    return False
        return len(stack) == 0

def flip(char):
    mystr = 'Tutorials Teacher'
    trans_dict = {'[':']', '{':'}', '(':')'}
    mytable = mystr.maketrans(trans_dict)
    return char.translate(mytable)
