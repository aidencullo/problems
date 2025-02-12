import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("11", "123"), "134"),
    (("456", "77"), "533"),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.addStrings(*test_input) == expected
