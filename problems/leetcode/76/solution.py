# time O(m*n)
# space O(1)

import math
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = [0] * 26
        window = [0] * 26
        left = 0
        min_len = math.inf
        for letter in t:
            need[ord(letter) % 26] += 1
        for right, letter in enumerate(s):
            if letter in t:
                window[ord(letter) % 26] += 1
            while compare(need, window):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_idx = left
                left_letter = s[left]
                if left_letter in t:
                    window[ord(left_letter) % 26] -= 1
                left += 1
        return s[min_idx:min_idx + min_len] if min_len != math.inf else ''

def compare(need, window):
    return all(need_count <= window_count for need_count, window_count in zip(need, window))
