class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not ch in word:
            return word
        ch_idx = word.index(ch)
        return word[:ch_idx + 1][::-1] + word[ch_idx + 1:]
