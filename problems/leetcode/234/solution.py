from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.current = None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pre_head = ListNode(0, head)
        head = pre_head
        second_head = pre_head
        while second_head:
            head = head.next
            second_head = second_head.next
            if second_head:
                second_head = second_head.next
        tail = self.reverseList(head)
        head = pre_head.next
        while tail:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head.next:
                return head
            tail = reverse(head.next)
            head.next.next = head
            return tail

        if not head:
            return None
        new_head = reverse(head)
        head.next = None
        return new_head
