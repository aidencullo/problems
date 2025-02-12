class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                current.children[letter] = self.TrieNode()
                current = current.children[letter]
        current.is_end_of_word = True
                

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return True


# # Your Trie object will be instantiated and called as such:
# word = 'apple'
# prefix = 'ap'
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# assert param_2
# param_3 = obj.startsWith(prefix)
# assert param_3
# param_4 = obj.startsWith('pa')
# assert not param_4
