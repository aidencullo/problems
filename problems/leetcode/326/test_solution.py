import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ((27, ), True),
    ((0, ), False),
    ((-1, ), False),
    ((9, ), True),
    ((1, ), True),
    ((43046721, ), True),
    ((243, ), True),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.isPowerOfThree(*test_input) == expected
