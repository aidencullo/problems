SIZE = 1000


class Entry:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.hashset = [Entry(-1)] * SIZE

    def add(self, key: int) -> None:
        entry = self.hashset[hash(key) % SIZE]
        while entry.next:
            if entry.next.key == key:
                return
            entry = entry.next
        entry.next = Entry(key)

    def remove(self, key: int) -> None:
        entry = self.hashset[hash(key) % SIZE]
        while entry.next:
            if entry.next.key == key:
                entry.next = entry.next.next
                return
            entry = entry.next

    def contains(self, key: int) -> bool:
        entry = self.hashset[hash(key) % SIZE]
        while entry.next:
            if entry.next.key == key:
                return True
            entry = entry.next
        return False

