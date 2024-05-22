import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ((2, [[1,2]],), 2),
])
def test_solution(test_input, expected):
    assert Solution().findJudge(*test_input) == expected
