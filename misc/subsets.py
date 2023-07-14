def subsets(array):
    if len(array) == 0:
        return [[]]
    results = [array]
    for item in array:
        tmp_array = [*array]
        tmp_array.remove(item)
        results += subsets(tmp_array)
    return results

subsets([1,2,3])
# [] [1] [2] [3] [1, 2, 3] [1, 2] [1, 3] [2, 3]
