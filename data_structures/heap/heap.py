"""
find-max (or find-min): find a maximum item of a max-heap, or a minimum item of a min-heap, respectively (a.k.a. peek)

insert: adding a new key to the heap (a.k.a., push[4])

extract-max (or extract-min): returns the node of maximum value from a max heap [or minimum value from a min heap] after removing it from the heap (a.k.a., pop[5])

delete-max (or delete-min): removing the root node of a max heap (or min heap), respectively

replace: pop root and push a new key. This is more efficient than a pop followed by a push, since it only needs to balance once, not twice, and is appropriate for fixed-size heaps.[6]
"""
from node import Node

class Heap:
    """
    Min Heap
    """

    def __init__(self):
        self.root = None

    def find_min(self):
        pass

    def insert(self, item):
        pass

    def extract_min(self):
        pass
 
    def delete_min(self):
        pass

    def replace(self):
        pass
