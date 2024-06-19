# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        while runner and runner.next:
            if runner.next.val == 0:
                runner.next = runner.next.next
                runner = runner.next
            else:
                runner.val += runner.next.val
                runner.next = runner.next.next
        return head
