def distance_pairs(k, numbers):
    hash_map = dict.fromkeys(numbers)
    return sum(i + k in hash_map for i in numbers)

distance_pairs(2, [1, 7, 5, 9, 12, 3]) # == 4
