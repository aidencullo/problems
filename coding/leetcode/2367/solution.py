# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = 0
        seen = set()
        for k in range(len(nums)):
            if nums[k] - diff in seen and nums[k] - 2 * diff in seen:
                cnt += 1
            seen.add(nums[k])
        return cnt
