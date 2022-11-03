import sys

def jump(nums: list[int]) -> int:
    hash_map={}
    min = 0
    l = len(nums)
    if l == 1:
        return 0
    array=[]
    fin=0
    for i in range(l):
        hash_map[i]=[]
        for x in reversed(range(1, nums[i] + 1)):
            if x + i < l-1:
                hash_map[i].append(x+i)
            else:
                fin=1
        origins = [key for key,value in hash_map.items() if i in value]
        if len(origins) > 0:
            min = sys.maxsize
        for y in origins:
            if array[y] + 1 < min:
                min = array[y] + 1
        array.append(min)
        if fin:
            return array[i] + 1
    return array[l-1]
            
        
def test(input, output):
    result = jump(input)
    if result == output:
        print("input ", input)
        print("SUCCESS")
    else:
        print("input ", input)
        print("FAILED: Expected: %d, Given: %d" % (output, result))

test([2,3,1,1,4], 2)
test([2,3,0,1,4], 2)
test([2,3,1,0,4], 2)
test([2,4], 1)
test([2,3,1,4], 2)
test([1,4], 1)
test([2,3,4], 1)
test([2,3,1,1,1,1], 3)
test([1],0)
test([100],0)
