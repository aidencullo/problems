# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_set = set()
        runner = headA
        while runner:
            hash_set.add(runner)
            runner = runner.next
        runner = headB
        while runner:
            if runner in hash_set:
                return runner
            runner = runner.next
        return None
