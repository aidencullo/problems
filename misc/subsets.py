import functools

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

def subsetsAlternative(array):
    return helper(array) + []

def helper(array):
    if len(array) == 0:
        return
    results = [array]
    for item in array:
        tmp_array = [*array]
        tmp_array.remove(item)
        recurse_results = subsets(tmp_array)
        for sub_item in recurse_results:
            if sub_item not in results:
                results.append(sub_item)
    return results

def compareList(list_a, list_b):
    if len(list_b) == len(list_a):
        for index in range(len(list_a)):
            if list_a[index] == list_b[index]:
                continue
            else:
                return list_a[index] - list_b[index]
    else:
        return len(list_a) - len(list_b)

result = subsets([1,2,3])
result = sorted(result, key=functools.cmp_to_key(compareList))
print(result)
# [] [1] [2] [3] [1, 2, 3] [1, 2] [1, 3] [2, 3]
