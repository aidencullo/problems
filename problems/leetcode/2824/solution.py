class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            pair_sum = nums[l] + nums[r]            
            if pair_sum < target:
                count += r - l
            if pair_sum >= target:
                r -= 1
            else:
                l += 1
        return count
