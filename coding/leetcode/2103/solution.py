from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for color, ring in grouper(rings, 2):
            rods[int(ring)].add(color)
        return sum(1 for rod in rods if len(rod) == 3)
