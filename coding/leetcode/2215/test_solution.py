import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,3], [2,4,6]), [[1,3],[4,6]]),
    ],
)
def test_single_node(test_input, expected):
    s = Solution()
    assert s.findDifference(*test_input) == expected
