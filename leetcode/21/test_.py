import pytest

from solution import ListNode, Solution

def test_single_node():
    # Arrange
    l = ListNode(1)
    l1 = ListNode(1)
    l1.next = l
    s = Solution()

    # Act
    result = s.mergeTwoLists(l, l)
    
    # Assert
    assert compareLL(result, l1)


def test_multiple_nodes():
    # Arrange
    l1 = ListNode(1)
    l2 = ListNode(4)
    l3 = ListNode(10)
    l4 = ListNode(100)
    l5 = ListNode(1000)
    l3.next = l5
    l1.next = l3
    l2.next = l4
    lresult1 = ListNode(1)
    lresult2 = ListNode(4)
    lresult3 = ListNode(10)
    lresult4 = ListNode(100)
    lresult5 = ListNode(1000)
    lresult1.next = lresult2
    lresult2.next = lresult3
    lresult3.next = lresult4
    lresult4.next = lresult5
    s = Solution()

    # Act
    result = s.mergeTwoLists(l1, l2)
    
    # Assert
    assert compareLL(result, lresult1)


def compareLL(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    if l1 or l2:
        return False
    return True
