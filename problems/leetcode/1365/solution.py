from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        nums_counter = Counter(nums)
        sorted_nums = sorted(nums_counter.items())
        prefix_sum = {}
        running_count = 0
        for num, count in sorted_nums:
            prefix_sum[num] = running_count
            running_count += count
        return [prefix_sum[num] for num in nums]
