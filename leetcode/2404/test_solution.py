import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([0,1,2,2,4,4,1],), 2),
        (([4,4,4,9,2,4],), 4),
        (([29,47,21,41,13,37,25,7],), -1),
    ],
)
def test_solution(test_input, expected):
    assert Solution().mostFrequentEven(*test_input) == expected
