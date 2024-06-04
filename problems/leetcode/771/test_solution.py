import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("aA", "aAAbbbb"), 3),
    (("z", "ZZ"), 0),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.numJewelsInStones(*test_input) == expected
