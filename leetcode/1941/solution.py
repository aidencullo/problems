class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import defaultdict
        appear = defaultdict(int)
        for c in s:
            appear[ord(c) - 97] += 1
        same = 0
        for value in appear:
            if same == 0:
                same = value
            else:
                if value != same:
                    return False
        return True
        