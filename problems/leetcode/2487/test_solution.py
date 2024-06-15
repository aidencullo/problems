# test_remove_nodes.py

import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        # This is the provided solution
        def reverse(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        head = reverse(head)
        dummy = ListNode()
        curr = dummy

        while head:
            if not curr.next or head.val > curr.next.val:
                curr.next = head
                head = head.next
                curr = curr.next
                curr.next = None
            else:
                head = head.next

        return reverse(dummy.next)

# Helper functions for testing
def list_to_linkedlist(items):
    dummy = ListNode()
    curr = dummy
    for item in items:
        curr.next = ListNode(item)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node):
    items = []
    while node:
        items.append(node.val)
        node = node.next
    return items

# Test cases
def test_remove_nodes():
    solution = Solution()

    head = list_to_linkedlist([5, 2, 13, 3, 8])
    expected = [13, 8]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

    head = list_to_linkedlist([1, 1, 1, 1])
    expected = [1, 1, 1, 1]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

    head = list_to_linkedlist([5, 4, 3, 2, 1])
    expected = [5]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

    head = list_to_linkedlist([1, 2, 3, 4, 5])
    expected = [5]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

    head = list_to_linkedlist([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    expected = [10]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

    head = list_to_linkedlist([1, 3, 2, 4, 3, 5])
    expected = [5]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

