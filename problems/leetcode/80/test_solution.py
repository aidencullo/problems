import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,1,1],), [1,1]),
        (([1,1,1,2,2,3],), [1,1,2,2,3]),
        (([0,0,1,1,1,1,2,3,3],), [0,0,1,1,2,3,3]),
        (([1,2,3],), [1,2,3]),
    ],
)
def test_solution(test_input, expected):
    Solution().removeDuplicates(*test_input)
    test_input, = test_input
    assert test_input == expected
