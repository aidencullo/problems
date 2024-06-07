class Entry:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.hashset = [None] * 1000001

    def add(self, key: int) -> None:
        if not self.hashset[hash(key)]:
            self.hashset[hash(key)] = Entry(key)
            return
        prev = Entry(-1)
        prev.next = self.hashset[hash(key)]
        entry = prev
        while entry.next:
            if entry.next.key == key:
                return
            entry = entry.next
        entry.next = Entry(key)

    def remove(self, key: int) -> None:
        if self.hashset[hash(key)] and self.hashset[hash(key)].key == key:
            self.hashset[hash(key)] = self.hashset[hash(key)].next
            return
        prev = Entry(-1)
        prev.next = self.hashset[hash(key)]
        entry = prev
        while entry.next:
            if entry.next.key == key:
                entry.next = entry.next.next
                return
            entry = entry.next

    def contains(self, key: int) -> bool:
        prev = Entry(-1)
        prev.next = self.hashset[hash(key)]
        entry = prev
        while entry.next:
            if entry.next.key == key:
                return True
            entry = entry.next
        return False
