from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        new_head = ListNode(float('-inf'), head)
        last = new_head
        runner = head
        while runner and runner.next:
            if runner.val == runner.next.val:
                while runner.next and runner.val == runner.next.val:
                    runner = runner.next
                last.next = runner.next
                runner = runner.next
            else:
                last = runner
                runner = runner.next
        return new_head.next
