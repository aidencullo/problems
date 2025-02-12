import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']), 5),
        (('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']), 0),
    ]
)
def testSolution(test_input, expected):
    sol = Solution()
    assert sol.ladderLength(*test_input) == expected
