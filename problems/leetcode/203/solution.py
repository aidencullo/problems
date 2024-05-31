from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
            self, head: Optional[ListNode],
            val: int
    ) -> Optional[ListNode]:
        pre_head = ListNode(0, head)
        runner = pre_head
        while runner.next:
            if runner.next.val == val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        return pre_head.next
