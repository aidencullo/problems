class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = ListNode()
        runner = head
        for i in range(1, n + 1):
            runner.next = ListNode(i)
            runner = runner.next
        runner.next = head.next
        current = head
        for i in range(1, n + 1):
            current = current.next
        while current.next != current:
            for i in range(k - 1):
                current = current.next
            current.next = current.next.next
        return current.val
