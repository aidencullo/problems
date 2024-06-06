import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ((["--X", "X++", "X++"],), 1),
    ((["++X", "++X", "X++"],), 3),
    ((["X++", "++X", "--X", "X--"],), 0),
])
def test_solution(test_input, expected):
    assert Solution().finalValueAfterOperations(*test_input) == expected
