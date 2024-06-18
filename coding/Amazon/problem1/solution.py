def max_collection(collections):
    rice_bags_sorted = dict.fromkeys(set(collections))
    max_rice_bag_size = 0
    for size in rice_bags_sorted:
        perfect = dict.fromkeys([size])
        while True:
            size *= size
            if size in rice_bags_sorted:
                perfect[size] = None
            else:
                break
        max_rice_bag_size = max(max_rice_bag_size, len(perfect))
        if max_rice_bag_size < 2:
            max_rice_bag_size = -1
    return max_rice_bag_size
