class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_NUMERALS = {
            '': 0,
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        
        total = 0
        i = 0
        n = len(s)
        while i < n:
            if i + 1 < n and s[i: i + 2] in ROMAN_NUMERALS:
                total += ROMAN_NUMERALS[s[i: i + 2]]
                i += 2
            else:
                total += ROMAN_NUMERALS[s[i]]
                i += 1
        return total