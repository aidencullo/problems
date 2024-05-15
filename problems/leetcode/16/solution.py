class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best_guess = 0
        square_diff = float('inf')
        for i, ele in enumerate(nums):
            l, r = i + 1, n - 1
            while l < r:
                guess = ele + nums[l] + nums[r]
                if guess == target:
                    return target
                diff = (guess - target) ** 2
                if diff < square_diff:
                    square_diff = diff
                    best_guess = guess
                if guess < target:
                    l += 1
                else:
                    r -= 1
        return best_guess
