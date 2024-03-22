import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([8,15,10,20,8], 2), 31),
        (([6,1,3,2,2,4,1,2], 3), 7),
        (([64,32,16,8,4,2,1,1000], 8), 1000),
    ]
)
def testSolution(test_input, expected):
    assert Solution().distributeCookies(*test_input) == expected
