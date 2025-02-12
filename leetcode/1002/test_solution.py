import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((["bella","label","roller"],), ["e","l","l"]),
        ((["cool","lock","cook"],), ["c","o"]),
    ],
)
def test_single_node(test_input, expected):
    s = Solution()
    assert s.commonChars(*test_input) == expected
