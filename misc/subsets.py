def subsets(array):
    if len(array) == 0:
        return []
    results = [array]
    for item in array:
        print(results)
        tmp_array = array
        results.append([item])
        tmp_array.remove(item)
        results.append(tmp_array)
    return results

print(subsets([1,2,3]))
# [] [1] [2] [3] [1, 2, 3] [1, 2] [1, 3] [2, 3]
