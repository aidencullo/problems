import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([1, 2, 2, 1], [2, 2]), [2, 2]),
])
def test_solution(test_input, expected):
    result = Solution().intersect(*test_input)
    assert result == expected
