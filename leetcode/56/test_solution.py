import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (
            (
                [[1,3],[2,6],[8,10],[15,18]],
            ),
            [[1,6],[8,10],[15,18]],
        ),
    ]

)
def testSolution(test_input, expected):
    assert Solution().merge(*test_input) == expected
