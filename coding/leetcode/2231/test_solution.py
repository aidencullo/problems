import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ((1234), 3412),
    ((65875), 87655),
    ])
def test_solution(test_input, expected):
    assert Solution().largestInteger(test_input) == expected
