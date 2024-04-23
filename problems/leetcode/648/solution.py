from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if not letter in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]                
        node.isEnd = True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def replace(word: str) -> str:
            res = ''
            runner = self.trie.root
            for letter in word:
                if letter in runner.children:
                    runner = runner.children[letter]
                    res += letter
                    if runner.isEnd:
                        return res
                else:
                     return word
            return word

        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word)
        replaced = [replace(word) for word in sentence.split()]
        return ' '.join(replaced)
