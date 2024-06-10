class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix = [sum(self.nums[:i+1]) for i in range(len(self.nums))]
            

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]
