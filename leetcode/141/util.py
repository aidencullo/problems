# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildCycleList(lst: list[int], pos: int):
    head = ListNode(0)
    current = head
    cycle = None
    for index, item in enumerate(lst):
         current.next = ListNode(item)
         current = current.next
         if index == pos:
             cycle = current
    current.next = cycle
    return head.next
