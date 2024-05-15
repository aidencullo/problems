from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        new_head = ListNode(0, head)
        m = 0
        runner = head
        while runner:
            m += 1
            runner = runner.next
        runner = new_head
        while runner:
            if m == n:
                runner.next = runner.next.next
                break
            runner = runner.next
            m -= 1
        return new_head.next
            
