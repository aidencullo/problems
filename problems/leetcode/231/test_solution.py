import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ((1, ), True),
    ((16, ), True),
    ((3, ), False),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.isPowerOfTwo(*test_input) == expected
