class Node:
    def __init__(self, key: int, value: int) -> None:
        self.value = value
        self.key = key
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.tail = None
        self.head = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            value = node.value
            self._delete(key)
            self._add(key, value)
            return value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete(key)
        self._add(key, value)
        if len(self.cache) > self.capacity:
            self._delete(self.head)

    def _delete(self, key: int) -> None:
        if len(self.cache) == 1:
            self.head = None
            self.tail = None
            del self.cache[key]
            return
        if key == self.head:
            next_key = self.cache[key].next
            self.cache[next_key].prev = None
            self.head = next_key
        elif key == self.tail:
            prev_key = self.cache[key].prev
            self.cache[prev_key].next = None
            self.tail = prev_key
        else:
            prev_key = self.cache[key].prev
            next_key = self.cache[key].next
            self.cache[prev_key].next = next_key
            self.cache[next_key].prev = prev_key
        del self.cache[key]

    def _add(self, key: int, value: int) -> None:
        self.cache[key] = Node(key, value)
        if len(self.cache) == 1:
            self.head = key
            self.tail = key
        else:
            self.cache[self.tail].next = key
            self.cache[key].prev = self.tail
            self.tail = key
            
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
