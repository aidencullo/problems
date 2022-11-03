import sys

def jump(nums: list[int]) -> int:
    hash_map={}
    min = 0
    array=[]
    for i in range(len(nums)):
        hash_map[i]=[]
        for x in range(1, nums[i] + 1):
            hash_map[i].append(x+i)
        origins = [key for key,value in hash_map.items() if i in value]
        if len(origins) > 0:
            min = sys.maxsize
        for y in origins:
            if array[y] + 1 < min:
                min = array[y] + 1
        array.append(min)
    return array[len(nums)-1]
            
        
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
