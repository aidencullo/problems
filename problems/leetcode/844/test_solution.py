import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("ab#c", "ad#c",), True),
    (("a##c", "#a#c",), True),
])
def test_solution(test_input, expected):
    s = Solution()
    result = s.backspaceCompare(*test_input)
    assert result == expected
