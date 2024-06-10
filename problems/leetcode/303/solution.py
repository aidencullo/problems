class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [sum(nums[:i]) for i in range(len(nums) + 1)]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
