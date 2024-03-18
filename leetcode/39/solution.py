from typing import Optional, List, Tuple

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationSumHelper(candidates, target):            
            if target == 0:
                return 0
            if target < 0:
                return -1
            results = []
            for candidate in candidates:
                subCombinationSum = combinationSumHelper(candidates,
                                                         target - candidate)



                if subCombinationSum == 0:
                    results.append([candidate])
                    continue
                if subCombinationSum == -1:
                    continue
                for comb in subCombinationSum:
                    results.append([candidate, *comb])
                    




            return results if results else -1
        results = combinationSumHelper(candidates, target)
        return results if results != -1 else []
