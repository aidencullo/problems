from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(path, rest):
            if not rest:
                self.res.append(path)
                return
            for i, el in enumerate(rest):
                helper(path + [el], rest[:i] + rest[i+1:])
        self.res = []
        helper([], nums)
        return self.res
