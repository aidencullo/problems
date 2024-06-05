class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = [0] * 26
        for char in s:
            letters[ord(char) - ord('a')] += 1
        for char in t:
            letters[ord(char) - ord('a')] -= 1
        for i, count in enumerate(letters):
            if count < 0:
                return chr(i + ord('a'))
