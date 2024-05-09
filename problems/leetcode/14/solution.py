from typing import List

import itertools


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = list(set(strs))
        strs.sort()
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            first = strs[0]
            last = strs[-1]
            if not first:
                return ""
            for i, (x, y) in enumerate(itertools.zip_longest(first, last)):
                if x != y:
                    return first[:i]
