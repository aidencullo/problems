import pytest
from solution import NumArray

def test_numarray():
    # Test case from the example
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    assert numArray.sumRange(0, 2) == 1, "Test case 1 failed"
    assert numArray.sumRange(2, 5) == -1, "Test case 2 failed"
    assert numArray.sumRange(0, 5) == -3, "Test case 3 failed"

    # Test with single element queries
    assert numArray.sumRange(0, 0) == -2, "Test case 4 failed"
    assert numArray.sumRange(3, 3) == -5, "Test case 5 failed"
    assert numArray.sumRange(5, 5) == -1, "Test case 6 failed"

    # Test with entire array
    assert numArray.sumRange(0, 5) == -3, "Test case 7 failed"
    
    # Test with different array configurations
    # All positive numbers
    numArray = NumArray([1, 2, 3, 4, 5])
    assert numArray.sumRange(0, 4) == 15, "Test case 8 failed"
    assert numArray.sumRange(1, 3) == 9, "Test case 9 failed"
    assert numArray.sumRange(2, 2) == 3, "Test case 10 failed"

    # All negative numbers
    numArray = NumArray([-1, -2, -3, -4, -5])
    assert numArray.sumRange(0, 4) == -15, "Test case 11 failed"
    assert numArray.sumRange(1, 3) == -9, "Test case 12 failed"
    assert numArray.sumRange(2, 2) == -3, "Test case 13 failed"

    # Mixed positive and negative numbers
    numArray = NumArray([1, -2, 3, -4, 5])
    assert numArray.sumRange(0, 4) == 3, "Test case 14 failed"
    assert numArray.sumRange(1, 3) == -3, "Test case 15 failed"
    assert numArray.sumRange(2, 2) == 3, "Test case 16 failed"
