from typing import List

class UnionFind:

    def __init__(self, n: int):
        self.rank = [1] * n
        self.parent = list(range(n))

    # O(logV)
    def union(self, u: int, v: int) -> None:
        u_rep = self.find(u)
        v_rep = self.find(v)
        if  u_rep == v_rep:
            return
        if self.rank[u_rep] < self.rank[v_rep]:
            self.rank[v_rep] += self.rank[u_rep]
            self.parent[u_rep] = v_rep
        else:
            self.rank[u_rep] += self.rank[v_rep]
            self.parent[v_rep] = u_rep

    # O(logV)
    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

# O(V^2 * logV)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for u in range(n):
            for v in range(n):
                if u != v and isConnected[u][v]:
                    uf.union(u, v)
        parents = set()
        for u in range(n):
            parents.add(uf.find(u))
        return len(parents)
