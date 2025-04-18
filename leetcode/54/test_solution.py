import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[1,2,3],[4,5,6],[7,8,9]],), [1,2,3,6,9,8,7,4,5]),
        (([[1,2,3,4],[5,6,7,8],[9,10,11,12]],), [1,2,3,4,8,12,11,10,9,5,6,7]),
        (([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],), [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]),
    ]
)
def testSolution(test_input, expected):
    assert Solution().spiralOrder(*test_input) == expected
