from itertools import chain
from functools import reduce
import operator

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return reduce(operator.xor, chain(nums, range(0, n + 1)))


"""
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

ideas:
- constant space
-- some preprocessing of some sort?
-- could still use a list of constant size
-- array of size 10k, mark visited, then find unvisited before a visited

- exploit the fact that number unique
- we know how many numbers need to be in the list
- swap values?
- what patterns are there?
-- a missing number in a list -- what does that equate to?
- what if we swapped the number with it's position in the list

ex:
[0 1 3 4]

[0 1 3 4]
[0 1 4 3]

- i think it will simply be the (n+1)(n/2) - sum(nums)
- would you like me to code it up?
"""
