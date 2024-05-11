class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            stack.append(i)
        if len(stack) < 2:
            nums.sort()
            return
        nums[stack[-1]], nums[stack[-2]] = nums[stack[-2]], nums[stack[-1]]
