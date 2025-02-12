import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ((1,), False),
    ((2,), True),
    ((3,), False),
    ((4,), True),
    ((5,), False),
    ((1000,), True),
])
def test_solution(test_input, expected):
    assert Solution().divisorGame(*test_input) == expected
