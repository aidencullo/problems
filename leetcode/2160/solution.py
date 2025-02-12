class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(list(str(num)))
        n = len(nums)
        l = [x for i, x in enumerate(nums) if i % 2 == 0]
        r = [x for i, x in enumerate(nums) if i % 2 == 1]
        return int(''.join(l)) + int(''.join(r))
