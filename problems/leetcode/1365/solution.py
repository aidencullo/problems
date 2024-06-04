from collections import defaultdict


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        counts = defaultdict(int)
        for num in nums: # O(n)
            counts[num] += 1
        return [less_than(num, counts) for num in nums] # O(n)


def less_than(num: int, counts: dict[int, int]) -> int:
    return sum(counts[x] for x in counts if x < num) # O(1) because there are at most 101 keys in counts
