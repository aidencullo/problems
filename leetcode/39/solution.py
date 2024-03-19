# Solution 1
# O(target) time and O(2^target) space

# from typing import Optional, List, Tuple

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         self.mem = {}
#         def subCombSum(target):
#             if target < 0:
#                 return []
#             results = []
#             for candidate in candidates:
#                 if target == candidate:
#                     results.append((candidate,))
#                 if target - candidate in self.mem:
#                     subComb = self.mem[target - candidate]
#                 else:
#                     subComb = subCombSum(target - candidate)
#                     self.mem[target - candidate] = subComb
#                 for comb in subComb:
#                     results.append((candidate, *comb))
#             return list(list(result) for result in set(tuple(sorted(result)) for result in results))
#         return subCombSum(target)





# Solution 2
# O(2^target) time and and space
from typing import Optional, List, Tuple

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def subCombSum(running, candidate_ptr, target):
            running = running[:]
            if candidate_ptr == len(candidates):
                return
            if target < 0:
                return
            if not target:
                self.res.append(running)
                return
            candidate = candidates[candidate_ptr]
            if candidate <= target:
                subCombSum(running + [candidate], candidate_ptr, target - candidate)
            subCombSum(running, candidate_ptr + 1, target)
        subCombSum([], 0, target)
        return self.res
