import pytest

from solution import Solution


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 3],), 6,),
        (([5, 1, 6],), 28,),
        (([3, 4, 5, 6, 7, 8],), 480,),
    ],
)
def test_solution(test_input, expected):
    assert Solution().subsetXORSum(*test_input) == expected
