from collections import defaultdict

class TreeNode:
    def __init__(self, val, timestamp, left=None, right=None):
        self.val = val
        self.timestamp = timestamp
        self.left = left
        self.right = right

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, val: str, timestamp: int) -> None:
        self.data[key].append((val, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data:
            return ""
        items = self.data[key]
        item_key = search(items, 0, len(items) - 1, timestamp)
        if item_key == -1:
            return ""
        return items[item_key][0]

def search(items, i, j, target_timestamp):
    if i > j:
        if j == -1:
            return -1
        if i == len(items) - 1:
            return j
        return j
    k = (j+i) // 2
    value, timestamp = items[k]
    if target_timestamp < timestamp:
        return search(items, i, k - 1, target_timestamp)
    if target_timestamp > timestamp:
        return search(items, k + 1, j, target_timestamp)
    return k
            
# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
obj.set("foo", "bar2", 2)
obj.set("foo", "bar3", 3)

param_2 = obj.get("foo", 2)
print(param_2) # bar2
param_3 = obj.get("foo", 3)
print(param_3) # bar3
param_1 = obj.get("foo", 1)
print(param_1) # bar
param_0 = obj.get("foo", 0)
print(param_0) # ""
