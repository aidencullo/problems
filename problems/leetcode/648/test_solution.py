import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((["cat", "bat", "rat"], "the cattle was rattled by the battery"), "the cat was rat by the bat"),
    ((["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"), "a a b c"),
])
def test_solution(test_input, expected):
    assert Solution().replaceWords(*test_input) == expected
