import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("YazaAay",), "aAa"),
        (("Bb",), "Bb"),
        (("c",), ""),
    ],
)
def test_solution(test_input, expected):
    assert Solution().longestNiceSubstring(*test_input) == expected
