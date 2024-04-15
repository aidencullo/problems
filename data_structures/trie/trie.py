class TrieNode:

    def __init__(self, children=None):
        if  children is None:
            children = {}
        self.children = children
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_entry(self, path: str):
        node = self.root
        for letter in path:
            if letter not in node.children:
                new_child = TrieNode()
                node.children[letter] = new_child
                node = new_child
            else:
                node = node.children[letter]
        node.isEnd = True    

    def is_entry(self, path: str):
        node = self.root
        for letter in path:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.isEnd

t = Trie()
t.add_entry('hello')
assert not t.is_entry('hell')
assert t.is_entry('hello')
