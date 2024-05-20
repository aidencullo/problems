class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        running = [1]
        for __ in range(numRows):
            result.append(running)
            last = running
            running = []
            for x, y in zip(last[1:], last):
                running.append(x + y)
            running = [1] + running + [1]
            last = running
        return result
