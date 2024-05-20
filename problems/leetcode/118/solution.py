class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        running = [1]
        for __ in range(numRows):
            result.append(running)
            running = [1] + [x + y for x, y in zip(running[1:], running)] + [1]
        return result
