import sys

min_glob = sys.maxsize
min_local = sys.maxsize

def jump(nums: list[int]) -> int:
    min_local=sys.maxsize
    if len(nums) == 1:
        return 0
    for x in range(nums[0]):
        if x + 1 < len(nums):
            min_new = 1 + jump(nums[x+1:])
            if min_new < min_local:
                min_local = min_new
    if min_local > min_global - 2:
        return sys.maxsize
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
