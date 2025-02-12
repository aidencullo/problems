class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not ch in word:
            return word
        ch_idx = word.index(ch)
        l, r = 0, ch_idx
        word = list(word)
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        return ''.join(word)
