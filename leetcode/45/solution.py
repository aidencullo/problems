import sys

min_glob = sys.maxsize
hash_map = []
def jump(nums: list[int]) -> int:
    if :
        return min_global
    min_glob
    if len(nums) == 1:
        return min_global = min_local
    for x in range(nums[0]):
        if x + 1 < len(nums):
            new_min = jump(nums[x+1:], min_local + 1)
            if new_min < min_global:
                min_global = min_new
    return min_global

def test(input, output):
    result = jump(input)
    if result == output:
        print("input ", input)
        print("SUCCESS")
    else:
        print("FAILED: Expected: %d, Given: %d" % (output, result))

test([2,3,1,1,4], 2)
test([2,3,0,1,4], 2)
test([2,3,1,0,4], 2)
test([2,4], 1)
test([2,3,1,4], 2)
test([1,4], 1)
test([2,3,4], 1)
test([2,3,1,1,1,1], 3)			       
