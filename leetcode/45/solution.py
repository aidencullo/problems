import sys


def jump(nums: list[int]) -> int:
    if nums[0] == 0:
        return sys.maxsize
    global min_global
    global min_local
    nlen = len(nums)
    if nlen == 1:
        min_global = min(min_global, min_local)
        return 0
    if min_local == min_global-1:
        return sys.maxsize
    current = nums[0]
    min_of_min = sys.maxsize
    min_local = min_local + 1
    for x in reversed(range(1, current + 1)):
        # check if the jump is too long
        if x < nlen:
            min_of_min = min(min_of_min, 1 + jump(nums[x:]))
        else:
            # here we have found another path
            min_global = min(min_global, min_local)
            min_of_min = min_local
    min_local = min_local - 1
    return min_of_min
        
def test(input, output):
    result = jump(input)
    if result == output:
        print("input ", input)
        print("SUCCESS")
    else:
        print("input ", input)
        print("FAILED: Expected: %d, Given: %d" % (output, result))

min_global = sys.maxsize
min_local = 0
test([2,3,1,1,4], 2)
min_global = sys.maxsize
min_local = 0
test([2,3,0,1,4], 2)
min_global = sys.maxsize
min_local = 0
test([2,3,1,0,4], 2)
min_global = sys.maxsize
min_local = 0
test([2,4], 1)
min_global = sys.maxsize
min_local = 0
test([2,3,1,4], 2)
min_global = sys.maxsize
min_local = 0
test([1,4], 1)
min_global = sys.maxsize
min_local = 0
test([2,3,4], 1)
min_global = sys.maxsize
min_local = 0
test([2,3,1,1,1,1], 3)
min_global = sys.maxsize
min_local = 0
test([1],0)
min_global = sys.maxsize
min_local = 0
test([100],0)
