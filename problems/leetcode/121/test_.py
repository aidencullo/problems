import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([2, 4, 1], 2),
    ],
)
def test_single_node(test_input, expected):
    result = Solution().maxProfit(test_input)
    assert result == expected
