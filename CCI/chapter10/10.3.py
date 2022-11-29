import time

sample = [16,19,20,25,1,3,4,5,7,10,100,101,1000]
sample1 = [1,2,3]
ans = 8

def search(array, value):
    start = find_start(array, 0, len(array)-1)
    return bin_search(array, value, start, 0, len(array)-1)

def bin_search(array, val, pivot, start, end):
    if start > end:
        print(val, "not found")
        return
    mid = (start + end)//2
    current = access(array, pivot, mid)
    if val < current:
        return bin_search(array, val, pivot, start, mid-1)
    elif val > current:
        return bin_search(array, val, pivot, mid+1, end)
    else:
        return mid + pivot


def access(array, start, index):
    return array[(start+index) % len(array)]
    
    
def find_start(array, start, end):
    mid = (start + end)//2
    mid_el = array[mid]
    end_el = array[end]
    if end - mid == 1 and mid_el > end_el:
        print("aca")
        return end
    if end - start == 1 and mid_el < end_el and start == 0:
        return mid
    if mid_el < end_el:
        # recurse on first half of array
        return find_start(array, start, mid)
    elif mid_el > end_el:
        #recurse on second half
        return find_start(array, mid, end)

print(search(sample, 5))
