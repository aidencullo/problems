from solution import KthLargest


import pytest

def test_kth_largest():
    # Initialize KthLargest with k = 3 and initial array [4, 5, 8, 2]
    kthLargest = KthLargest(3, [4, 5, 8, 2])

    # Add elements and check the kth largest element after each addition
    assert kthLargest.add(3) == 4  # After adding 3, the 3rd largest element is 4
    assert kthLargest.add(5) == 5  # After adding 5, the 3rd largest element is 5
    assert kthLargest.add(10) == 5  # After adding 10, the 3rd largest element is 5
    assert kthLargest.add(9) == 8  # After adding 9, the 3rd largest element is 8
    assert kthLargest.add(4) == 8  # After adding 4, the 3rd largest element is 8

def test_leet():
    kthLargest = KthLargest(1, [])
    assert kthLargest.add(-3) == -3
    assert kthLargest.add(-2) == -2
    assert kthLargest.add(-4) == -2
    assert kthLargest.add(0) == 0
    assert kthLargest.add(4) == 4
    
