class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.hashset = [None] * self.capacity


    def put(self, key: int, value: int) -> None:
        hash_key = hash(key) % self.capacity
        entry = self.hashset[hash_key]
        if self.contains(key):
            self.insert(entry, key, value)
            return
        if not entry:
            self.hashset[hash_key] = Entry(key, value)
        else:
            self.insert(entry, key, value)
        self.size += 1
        self._resize()

    def _put(self, key: int, value: int) -> None:
        hash_key = hash(key) % self.capacity
        entry = self.hashset[hash_key]
        if self.contains(key):
            self.insert(entry, key, value)
            return
        if not entry:
            self.hashset[hash_key] = Entry(key, value)
        else:
            self.insert(entry, key, value)

    def remove(self, key: int) -> None:
        hash_key = hash(key) % self.capacity
        entry = self.hashset[hash_key]
        if not entry:
            return
        if entry.key == key:
            self.hashset[hash_key] = entry.next
            self.size -= 1
            return
        while entry.next:
            if entry.next.key == key:
                entry.next = entry.next.next
                self.size -= 1
                return
            entry = entry.next

    def get(self, key: int) -> int:
        hash_key = hash(key) % self.capacity
        entry = self.hashset[hash_key]
        if not entry:
            return -1
        if entry.key == key:
            return entry.value
        while entry.next:
            if entry.next.key == key:
                return entry.next.value
            entry = entry.next
        return -1

    def contains(self, key: int) -> bool:
        hash_key = hash(key) % self.capacity
        entry = self.hashset[hash_key]
        while entry:
            if entry.key == key:
                return True
            entry = entry.next
        return False

    def insert(self, entry, key, value):
        if entry.key == key:
            entry.value = value
            return
        while entry.next:
            if entry.next.key == key:
                entry.next.value = value
                return
            entry = entry.next
        entry.next = Entry(key, value)

    def _resize(self):
        if self._load_factor() < .5:
            return
        self.capacity *= 2
        new_hashset = self.hashset[:]
        self.hashset = [None] * self.capacity
        for key_hash in new_hashset:
            while key_hash:
                self._put(key_hash.key, key_hash.value)
                key_hash = key_hash.next

    def _load_factor(self):
        return self.size / self.capacity
