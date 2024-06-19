import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        while runner.next:
            lcm_node = ListNode(math.gcd(runner.val, runner.next.val))
            lcm_node.next = runner.next
            runner.next = lcm_node
            runner = runner.next.next
        return head
