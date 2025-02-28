from typing import Optional



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre_head = ListNode(0, next=head)
        right = pre_head
        left = pre_head
        for x in range(n):
            right = right.next
        
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next

        return pre_head.next
    