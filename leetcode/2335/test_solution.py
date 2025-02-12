import pytest

from solution import Solution

def test_fillCups():
    solution = Solution()
    
    # Test case 1
    assert solution.fillCups([1, 4, 2]) == 4
    
    # Test case 2
    assert solution.fillCups([5, 4, 4]) == 7
    
    # Test case 3
    assert solution.fillCups([5, 0, 0]) == 5
    
    # Additional test cases
    assert solution.fillCups([0, 0, 0]) == 0
    assert solution.fillCups([3, 3, 3]) == 5
    assert solution.fillCups([1, 1, 1]) == 2

