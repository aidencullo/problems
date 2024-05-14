import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("aaabc", ), 3),
        (("cbbd", ), 3),
        (("dddaaa", ), 2),
        (("ipi", ), 2),
    ],
)
def test_solution(test_input, expected):
    assert Solution().minimizedStringLength(*test_input) == expected
