class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        normal = list(range(1, n + 1))
        diff = sum(normal) - sum(nums)
        square = lambda x: x ** 2
        diff2 = sum(map(square, normal)) - sum(map(square, nums))
        missing = ((diff2 // diff ) + diff) // 2
        duplicate = missing - diff
        return [duplicate, missing]
