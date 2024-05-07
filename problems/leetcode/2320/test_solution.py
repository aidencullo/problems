import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((1,), 4),
    ((2,), 9),
    ((3,), 25),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.countHousePlacements(*test_input) == expected
