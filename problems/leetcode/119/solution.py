from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        pascal = self.getRow(rowIndex - 1)
        return [1] + [pascal[i] + pascal[i + 1] for i in range(len(pascal) - 1)] + [1]
