import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([1, 5, 0, 3, 5],), 3),
    (([0],), 0),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.minimumOperations(*test_input) == expected
