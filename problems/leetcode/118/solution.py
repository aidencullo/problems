from itertools import zip_longest

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        running = self.generate(numRows - 1)
        last = running[-1]
        next = [x + y for x, y in zip_longest([0] + last, last, fillvalue=0)]
        return running + [next]
