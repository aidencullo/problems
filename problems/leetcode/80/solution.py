class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r = 0, 0
        current = float('inf')
        count = 0
        while r < len(nums):
            if count == 2:
                while r < len(nums) and nums[r] == current:
                    r += 1
                if r == len(nums):
                    break
                current = nums[r]
                count = 1
            else:
                if current != nums[r]:
                    count = 1
                    current = nums[r]
                else:
                    count += 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        del nums[l:]
