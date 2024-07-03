class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        d = list(enumerate(nums))
        d.sort(key=lambda x: x[1])
        d = d[-k:]
        d.sort(key=lambda x: x[0])
        return [y for x, y in d]
