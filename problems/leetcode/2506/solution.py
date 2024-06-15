class Solution:
    def similarPairs(self, words: list[str]) -> int:
        def isSimilar(wordA, wordB):
            return set(wordA) == set(wordB)
        
        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if isSimilar(words[i], words[j]):
                    cnt += 1
        return cnt
                        
