class Solution:
    def intToRoman(self, n: int) -> str:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]
        res = []
        res.append(thousands[n // 1000])
        res.append(hundreds[n // 100 % 10])
        res.append(tens[n // 10 % 10])
        res.append(ones[n % 10])
        return "".join(res)
