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
        last = ''
        for c in s:
            if ROMAN_NUMERALS[c] > ROMAN_NUMERALS[last] and last != '':
                total += ROMAN_NUMERALS[c] - 2 * ROMAN_NUMERALS[last]
            else:
                total += ROMAN_NUMERALS[c]
            last = c
        return total
                