# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n) time and O(1) space
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one_step = head
        two_step = head
        while two_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next
            if two_step:
                two_step = two_step.next
        return two_step
