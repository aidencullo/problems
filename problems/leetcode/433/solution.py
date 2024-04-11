# time O(m*n) m is the length of startGene, n is the length of bank
# space O(n) n is the length of bank

from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        choices = 'ACGT'
        bank = set(bank)
        q = deque([startGene])
        count = -1
        while q:
            count += 1
            qlen = len(q)
            for __ in range(qlen):
                gene = q.popleft()
                if gene == endGene:
                    return count
                for choice in choices:
                    for i in range(len(gene)):
                        newGene = gene[:i] + choice + gene[i+1:]
                        if newGene in bank:
                            q.append(newGene)
                            bank.remove(newGene)
        return -1
