from itertools import zip_longest
from collections import defaultdict


def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)
        for color, ring in grouper(rings, 2):
            rods[ring].add(color)
        return sum(1 for rod in rods if len(rods[rod]) == 3)
