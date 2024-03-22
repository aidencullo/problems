# from typing import List

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 1:
#             return [nums]
#         res = []
#         seen = set()
#         for i, num in enumerate(nums):
#             if num in seen:
#                 continue
#             for perm in self.permuteUnique(nums[:i] + nums[i + 1:]):
#                 res.append([num, *perm])
#             seen.add(num)
#         return res


from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permuteUniqueHelper(hash_map: dict[int, int], permutation):
            if not any(hash_map.values()):
                self.permutations.append(permutation[:])
                return
            for key in hash_map:
                if hash_map[key]:
                    permutation.append(key)
                    hash_map[key] -= 1
                    permuteUniqueHelper(hash_map, permutation)
                    hash_map[key] += 1
                    permutation.pop()
        self.permutations = []
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        permuteUniqueHelper(hash_map, [])
        return self.permutations
