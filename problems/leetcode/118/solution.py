class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        running = self.generate(numRows - 1)
        last = running[-1]
        next = [1] + [x + y for x, y in zip(last[1:], last)] + [1]
        return running + [next]
