class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_NUMERALS = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        last = 0
        for c in reversed(s):
            val = ROMAN_NUMERALS[c]
            if val < last:
                total -= val
            else:
                total += val
            last = val
        return total
                