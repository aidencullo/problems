import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([1, 3, 4], [1, 3, 4], 1), 5),
    (([1, 2, 4, 12], [2, 4], 3), 2),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.numberOfPairs(*test_input) == expected
