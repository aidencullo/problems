class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = [0] * 26
        for char in sentence:
            letters[ord(char) % 26] += 1
        return all(quantity != 0 for quantity in letters)
