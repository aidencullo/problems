class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key=lambda x: int(x[-1]))
        s = [word[:-1] for word in s]
        return ' '.join(s)
