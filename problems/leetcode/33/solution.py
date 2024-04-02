# O(log n) time and space

from typing import Optional, List, Tuple

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        starting_index = find_start(nums)
        return find_target(nums, target, starting_index)

def find_start(nums):
    def find_start_helper(l, r, lst):
        m = (l+r) // 2
        left = lst[l]
        right = lst[r]
        middle = lst[m]
        if left > middle:
            return find_start_helper(l + 1, m, lst)
        if middle > right:
            return find_start_helper(m + 1, r, lst)
        return l
    return find_start_helper(0, len(nums) - 1, nums)

def find_target(nums, target, offset):
    def find_target_helper(l, r, lst, val):
        if l > r:
            return -1
        m = (l+r) // 2
        middle = lst[(m + offset) % len(nums)]
        if val > middle:
            return find_target_helper(m + 1, r, lst, val)
        if val < middle:
            return find_target_helper(l, m - 1, lst, val)
        return (m + offset) % len(nums)
    return find_target_helper(0, len(nums) - 1, nums, target)

