from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        choices = 'ACGT'
        def bfs(firstGene):
            q = deque()
            q.append(firstGene)
            count = -1
            seen = []
            while q:
                count += 1
                qlen = len(q)
                for __ in range(qlen):
                    gene = q.popleft()
                    if gene == endGene:
                        return count
                    seen.append(gene)
                    for choice in choices:
                        for i in range(len(gene)):
                            newGene = gene[:i] + choice + gene[i+1:]
                            if newGene in bank and newGene not in seen:
                                q.append(newGene)
            return -1
                            
        return bfs(startGene)
