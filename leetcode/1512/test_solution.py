import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ([1, 2, 3, 1, 1, 3], 4),
    ([1, 1, 1, 1], 6),
    ([1, 2, 3], 0),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.numIdenticalPairs(test_input) == expected
