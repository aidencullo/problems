def intersect(i1: tuple[int, int], i2: tuple[int, int]):
    return i1[1] >= i2[0] and i2[1] >= i1[0]

        
def combine(i1: tuple[int, int], i2: tuple[int, int], i3: tuple[int, int]):
    if not i3:
        i3 = [float('inf'), float('-inf')]
    return [min(i1[0], i2[0], i3[0]), max((i1[1], i2[1], i3[1]))]
