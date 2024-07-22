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
        while head.next.next:
            for i in range(k - 1):
                if current.next:
                    current = current.next
                else:
                    current = head.next
            if not current.next.next
            current.next = current.next.next
        return head.next.val
