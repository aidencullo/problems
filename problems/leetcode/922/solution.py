class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x % 2 != 0]
        return [odd.pop() if i % 2 else even.pop() for i in range(len(nums))]
