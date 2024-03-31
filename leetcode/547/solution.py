# time: O(n^2)
# space: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node): 
            visited.add(node)
            for neighbor, connected in enumerate(isConnected[node]):
                if connected and neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i)
        return provinces
