from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(float('-inf'), head)
        runner = new_head
        while runner.next:
            if runner.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        return new_head.next
