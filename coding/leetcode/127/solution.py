from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        wordList = set(wordList)
        q = deque([beginWord])
        count = 0
        while q:
            count += 1
            qlen = len(q)
            for __ in range(qlen):
                word = q.popleft()
                if word == endWord:
                    return count
                for letter in alphabet:
                    for position in range(len(word)):
                        newWord = word[:position] + letter + word[position+1:]
                        if newWord in wordList:
                            q.append(newWord)
                            wordList.remove(newWord)
        return 0
