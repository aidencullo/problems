# Sol 1: iterate over s comparing frequencies of p with current p-size window

# time: O(s*p) space: O(p)

# from collections import Counter
# from typing import List

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         if len(s) < len(p):
#             return []
#         if not p:
#             return []
#         p_counter = Counter(p) # O(p)
#         res = []
#         for i in range(len(s) - len(p) + 1): # O(s)
#             s_counter = Counter(s[i:i+len(p)]) # O(p)
#             if p_counter == s_counter: # O(p)
#                 res.append(i) # O(1)
#         return res          





# Sol 2: really the same as Sol 1 but more explicitly create counter with array of possible char values

# time O(s + p) = O(s)
# space O(1)

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): # O(1)
            return []
        if not p:
            return []
        res = []
        s = s.lower() # O(s)
        p = p.lower() # O(p)
        p_counter = [0] * 26 # O(1)
        s_counter = [0] * 26 # O(1)
        for letter in p: # O(p)
            p_counter[ord(letter) - ord('a')] += 1
        s_counter = [0] * 26 # O(1)
        for i in range(len(s)): # O(s)
            s_counter[ord(s[i]) - ord('a')] += 1 # O(1)
            if i >= len(p): # O(1)
                s_counter[ord(s[i - len(p)]) - ord('a')] -= 1 # O(1)
            if all(x == y for x,y in zip(p_counter, s_counter)): # O(1)
                res.append(i - len(p) + 1) # O(1)
        return res          
