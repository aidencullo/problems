def getSubsets(array):
    if len(array) == 0:
        return [[]]
    results = [array]
    for item in array:
        tmp_array = [*array]
        tmp_array.remove(item)
        results += subsets(tmp_array)
    return results

def subsets(array):
    return unique(getSubsets(array))

def unique(array):
    set_from_list = {tuple(i) for i in array}
    list_from_set = [list(i) for i in set_from_list]
    return list_from_set

subsets([1,2,3])
# [] [1] [2] [3] [1, 2, 3] [1, 2] [1, 3] [2, 3]
