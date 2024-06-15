from solution import Solution, ListNode


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
    expected = [5, 4, 3, 2, 1]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

    head = list_to_linkedlist([1, 2, 3, 4, 5])
    expected = [5]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

    head = list_to_linkedlist([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

    head = list_to_linkedlist([1, 3, 2, 4, 3, 5])
    expected = [5]
    result = solution.removeNodes(head)
    assert linkedlist_to_list(result) == expected

