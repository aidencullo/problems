from typing import Optional, List, Tuple

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.mem = {}
        def subCombSum(target):
            if target < 0:
                return []
            results = []
            for candidate in candidates:
                if target == candidate:
                    results.append((candidate,))
                if target - candidate in self.mem:
                    subComb = self.mem[target - candidate]
                else:
                    subComb = subCombSum(target - candidate)
                    self.mem[target - candidate] = subComb
                for comb in subComb:
                    results.append((candidate, *comb))
            return list(list(result) for result in set(tuple(sorted(result)) for result in results))
        return subCombSum(target)
