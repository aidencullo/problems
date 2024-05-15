
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return reduce(operator.xor, itertools.chain(range(1, len(nums)), nums)
