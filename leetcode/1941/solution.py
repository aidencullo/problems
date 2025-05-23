class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        appear = [0] * 26
        for c in s:
            appear[ord(c) - 97] += 1
        same = 0
        for value in appear:
            if value > 0:
                if same == 0:
                    same = value
                else:
                    if value != same:
                        return False
        return True
        