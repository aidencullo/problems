import itertools

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        subtraction = {
            'IV': -1,
            'IX': -1,
            'XL': -10,
            'XC': -10,
            'CD': -100,
            'CM': -100,
        }
        result = 0

        for x, y in itertools.zip_longest(s, s[1:] + 'I'):
            if x + y in subtraction:
                result += subtraction[x + y]
            else:
                result += values[x]        
        return result
