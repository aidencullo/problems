# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        runner = list1
        for i in range(1, a):
            runner = runner.next
        for i in range(a, b + 1):
            runner.next = runner.next.next
        runner2 = list2
        while runner2.next:
            runner2 = runner2.next        
        runner = list1
        for i in range(1, a):
            runner = runner.next
        runner2.next = runner.next
        runner.next = list2
        return list1
