# time: O(n)
# space: O(n)


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        opposite = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        closing = set((
            ')',
            ']',
            '}',
        ))
        for symbol in s:
            if symbol in closing:
                if not stack or stack.pop() != symbol:
                    return False
            else:
                stack.append(opposite[symbol])
        return not stack
