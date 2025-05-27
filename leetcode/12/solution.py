class Solution:
    def intToRoman(self, n: int) -> str:
        roman_numeral = []
        if n >= 1000:
            roman_numeral.append("M" * (n // 1000))
            n %= 1000
        if n >= 900:
            roman_numeral.append("CM")
            n %= 900
        if n >= 500:
            roman_numeral.append("D")
            n %= 500
        if n >= 400:
            roman_numeral.append("CD")
            n %= 400
        if n >= 100:
            roman_numeral.append("C" * (n // 100))
            n %= 100
        if n >= 90:
            roman_numeral.append("XC")
            n %= 90
        if n >= 50:
            roman_numeral.append("L" * (n // 50))
            n %= 50
        if n >= 40:
            roman_numeral.append("XL")
            n %= 40
        if n >= 10:
            roman_numeral.append("X" * (n // 10))
            n %= 10
        if n >= 9:
            roman_numeral.append("IX")
            n %= 9
        if n >= 5:
            roman_numeral.append("V")
            n %= 5
        if n >= 4:
            roman_numeral.append("IV")
            n %= 4
        if n >= 1:
            roman_numeral.append("I" * n)
            n %= 1
        return "".join(roman_numeral)