# Sol 1: iterate over s comparing frequencies of p with current p-size window

# time: O(s*p) space: O(p)

from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        if not p:
            return []
        p_counter = Counter(p) # O(p)
        res = []
        for i in range(len(s) - len(p) + 1): # O(s)
            s_counter = Counter(s[i:i+len(p)]) # O(p)
            if p_counter == s_counter: # O(p)
                res.append(i) # O(1)
        return res          
