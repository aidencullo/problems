import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([0,1,7,6,0,2,0,7],), [0, 0, 1, 7, 6, 0, 0, 2]),
        (([1, 0, 2, 3, 0, 4, 5, 0],), [1, 0, 0, 2, 3, 0, 0, 4]),
        (([1,0,2,3,0,4,5,0],), [1, 0, 0, 2, 3, 0, 0, 4]),
        (([1, 2, 3],), [1, 2, 3]),
    ],
)
def test_solution(test_input, expected):
    Solution().duplicateZeros(*test_input)
    test_input, = test_input
    assert test_input == expected
