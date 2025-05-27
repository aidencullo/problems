class Solution:
    def intToRoman(self, n: int) -> str:
        val_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
        roman = []
        for val in sorted(val_map.keys(), reverse=True):
            count = n // val
            if count:
                roman.append(val_map[val] * count)
                n %= val
        return "".join(roman)
