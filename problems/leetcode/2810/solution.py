from collections import deque


class Solution:
    def finalString(self, s: str) -> str:
        deq = deque()
        front = False
        for letter in s:
            if letter == 'i':
                front = not front
            else:
                if front:
                    deq.appendleft(letter)
                else:
                    deq.append(letter)
        return "".join(deq) if not front else "".join(deq)[::-1]
