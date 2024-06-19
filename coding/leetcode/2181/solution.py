class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head.next
        new_head = ListNode(0)
        new_runner = new_head
        total = 0
        while runner:
            if runner.val != 0:
                total += runner.val
            else:
                new_runner.next = ListNode(total)
                new_runner = new_runner.next
                total = 0
            runner = runner.next
        return new_head.next
