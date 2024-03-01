def binary_search(elements, target):
    n = len(elements)
    def search_by_index(lower, upper):
        if upper < lower:
            return lower

        k = (upper + lower) // 2
        current = elements[k]
        
        if current < target:
            return search_by_index(k + 1, upper)
        if current > target:
            return search_by_index(lower, k - 1)
        return k
    return search_by_index(0, n - 1)
