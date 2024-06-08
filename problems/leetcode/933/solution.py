class Entry:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.hashset = [None] * self.capacity

    def add(self, key: int) -> None:
        if not self.hashset[hash(key) % self.capacity]:
            self.hashset[hash(key) % self.capacity] = Entry(key)
            self.size += 1
            self._resize()
            return
        entry = self.hashset[hash(key) % self.capacity]
        while entry.next:
            if entry.next.key == key:
                return
            entry = entry.next
        entry.next = Entry(key)
        self.size += 1
        self._resize()

    def remove(self, key: int) -> None:
        entry = self.hashset[hash(key) % self.capacity]
        if not entry:
            return
        if entry.key == key:
            self.hashset[hash(key) % self.capacity] = entry.next
            self.size -= 1
            return
        while entry.next:
            if entry.next.key == key:
                entry.next = entry.next.next
                self.size -= 1
                return
            entry = entry.next

    def contains(self, key: int) -> bool:
        entry = self.hashset[hash(key) % self.capacity]
        while entry:
            if entry.key == key:
                return True
            entry = entry.next
        return False

    def _resize(self):
        if self._load_factor() < .5:
            return
        self.capacity *= 2
        new_hashset = self.hashset[:]
        self.hashset = [None] * self.capacity
        for key_hash in new_hashset:
            while key_hash:
                self.add(key_hash.key)
                key_hash = key_hash.next

    def _load_factor(self):
        return self.size / self.capacity
