from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]
        for __ in range(rowIndex):
            new_pascal = []
            new_pascal.append(1)
            for j in range(len(pascal) - 1):
                new_pascal.append(pascal[j] + pascal[j + 1])
            new_pascal.append(1)
            pascal = new_pascal
        return pascal
