# time: O(4^n) where n is the number of digits in the input

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def letterCombinationsHelper(num_index: int, running_str: str) -> List[str]:
            if num_index == len(digits):
                if running_str:
                    self.res.append(running_str)
                return
            letters = telephone[digits[num_index]]
            for letter in letters:
                letterCombinationsHelper(num_index + 1, running_str + letter)
        telephone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.res = []
        letterCombinationsHelper(0, "")
        return self.res
