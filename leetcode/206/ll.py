# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_ll(lst):
    head: ListNode = ListNode()
    current = head
    for item in lst:
        current.next = ListNode(item)
        current = current.next
    return head.next


def ll_to_list(ll):
    current: ListNode = ll
    lst = []
    while current:
        lst.append(current.val)
        current = current.next
    return lst
