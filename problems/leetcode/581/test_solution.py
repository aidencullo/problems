import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 2, 3, 4],), 0),
        (([2, 6, 4, 8, 10, 9, 15],), 5),
        (([1,2,3,3,3],), 0),
        (([1,3,2,2,2],), 4),
        (([1,2,5,3,4],), 3),
        (([2,3,3,2,4],), 3),
        (([1,3,2,3,3],), 2),
        (([1,3,4,2,5],), 3),
    ],
)
def test_solution(test_input, expected):
    assert Solution().findUnsortedSubarray(*test_input) == expected
    
