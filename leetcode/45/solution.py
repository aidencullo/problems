import sys

def jump(nums: list[int]) -> int:
    min = sys.maxsize
    if len(nums) == 1:
        return 0
    for x in range(nums[0]):
        if x + 1 < len(nums):
            new_min = 1 + jump(nums[x+1:])
            if new_min < min:
                min = new_min
    return min

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
