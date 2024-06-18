class NumArray:

    def __init__(self, nums: list[int]):
        total = 0
        self.prefix = []
        for num in nums:
            self.prefix.append(total)
            total += num
        self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
