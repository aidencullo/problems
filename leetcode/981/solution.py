 class TreeNode:
    def __init__(self, val, timestamp, left=None, right=None):
        self.val = val
        self.timestamp = timestamp
        self.left = left
        self.right = right

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, val: str, timestamp: int) -> None:
        if not key in self.data:
            self.data[key] = TreeNode(val, timestamp)
            return
        n = self.data[key]
        while 1:
            if timestamp > n.timestamp:
                if n.right:
                    n = n.right
                else:
                    n.right = TreeNode(val, timestamp)
                    return
            if timestamp < n.timestamp:
                if n.left:
                    n = n.left
                else:
                    n.left = TreeNode(val, timestamp)
                    return
            if timestamp == n.timestamp:
                n.val = val
                return

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data:
            return ""
        n = self.data[key]
        while 1:
            if timestamp < n.timestamp:
                if n.left:
                    n = n.left
                else:
                    return ""
            if timestamp > n.timestamp:
                if n.right:
                    if timestamp >= n.right.timestamp:
                        n = n.right
                    else:
                        return n.val
                else:
                    return n.val
            if timestamp == n.timestamp:
                return n.val
 
            
# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "bar", 1)
obj.set("foo", "bar2", 2)
obj.set("foo", "bar3", 3)
param_2 = obj.get("foo", 2)
print(param_2) # bar2
