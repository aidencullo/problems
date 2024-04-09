# time O(m + n)
# space O(26) == O(1)

import math
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)
        left = 0
        valid_cnt = 0
        min_len = math.inf
        for right, letter in enumerate(s):
            if window[letter] < need[letter]:
                valid_cnt += 1
            window[letter] += 1
            while valid_cnt == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_idx = left
                if window[s[left]] == need[s[left]]:
                    valid_cnt -= 1
                window[s[left]] -= 1
                left += 1
        return s[min_idx:min_idx + min_len] if min_len != math.inf else ''
