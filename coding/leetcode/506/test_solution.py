import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([5,4,3,2,1],), ["Gold Medal","Silver Medal","Bronze Medal", "4", "5"]),
    (([10,3,8,9,4],), ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
])
def test_solution(test_input, expected):
    assert list(Solution().findRelativeRanks(*test_input)) == expected
