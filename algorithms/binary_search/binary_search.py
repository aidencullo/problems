def binary_search(elements, target):
    def search_by_index(lower, upper):
        k = (upper + lower) // 2
        current = elements[k]
        
        if upper < lower:
            return upper        
        if current < target:
            return search_by_index(k + 1, upper)
        if current > target:
            return search_by_index(lower, k - 1)
        return k
    return search_by_index(0, len(elements) - 1)
