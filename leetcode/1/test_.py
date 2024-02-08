import pytest

from solution import Solution

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (([3, 2, 4], 6), [1, 2]),    
        (([3, 3], 6), [0, 1]),
        (([2, 7, 11, 15], 9), [0, 1]),
    ],
)
def test(test_input, expected):
    s = Solution()
    assert s.twoSum(*test_input) == expected
