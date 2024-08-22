from solution import Solution

assert Solution().kthSmallest([[1,1,3,8,13],[4,4,4,8,18],[9,14,18,19,20],[14,19,23,25,25],[18,21,26,28,29]], 13) == 18
assert Solution().kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 5) == 7
assert Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13
assert Solution().kthSmallest([[-5]], 1) == -5
assert Solution().kthSmallest([[1,2],[1,3]], 4) == 3
