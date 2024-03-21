# time: O(n)
# space: O(n)
# n = len(s)


from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakHelper(start_index: int) -> bool:
            if start_index == len(s):
                return True
            if start_index in self.memo:
                return self.memo[start_index]
            for word in wordDict:
                if s[start_index: start_index + len(word)] == word:
                    if wordBreakHelper(start_index + len(word)):
                        self.memo[start_index] = True
                        return True
            self.memo[start_index] = False
            return False
        self.memo = {}
        wordDict.sort(key=lambda x: len(x), reverse=True)
        return wordBreakHelper(0)    
