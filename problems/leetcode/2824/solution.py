class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        count = 0
        for i, ele in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            sub_target = target - ele - 1
            while l <= r:
                k = (r + l) // 2
                middle = nums[k]
                if middle <= sub_target:
                    l = k + 1
                else:
                    r = k - 1
            count += r - i
        return count
