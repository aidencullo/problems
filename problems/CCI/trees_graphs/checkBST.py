class Tree:

    def __init__(self, array):
        self.root = None
        for x in array:
            self.insert(x)
            
    def BST(self):
        return self.checkBST(self.root)

    def checkBST(self, node):
        if not node:
            return True
        if not self.checkBST(node.left) or not self.checkBST(node.right):
            return False
        if abs(self.checkHeight(node.left) - self.checkHeight(node.right)) <= 1:
            return True
        else:
            return False

    def checkHeight(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.checkHeight(node.left), self.checkHeight(node.right))

    def insert(self, number):
        if not self.root:
            self.root = Node(number)
            return
        node  = self.root
        while(node.left and node.right):
            node = node.left
        if not node.left:
            node.left = Node(number)
        else:
            node.right = Node(number)

    def show(self):
        self.root.print()

    def test(self):
        print(self.BST())
        
class Node:
    left = right = None
    val = -1

    def __init__(self, value):
        self.val = value

    def print(self):
        if self.val == -1:
            return
        print(self.val)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()



t = Tree([1,2,3,4])
t.test()
print(t.BST())

t1 = Tree([0])
t1.root.left = Node(1)
t1.root.right = Node(2)

t1.test()
t1.root.right.right = Node(3)
t1.test()
t1.root.right.right.right = Node(4)
t1.test()
