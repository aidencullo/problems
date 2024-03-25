import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,3],), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ]
)
def testSolution(test_input, expected):
    actual = Solution().subsets(*test_input)
    for i in actual:
        assert any(set(i) == set(j) for j in expected)
    for i in expected:
        assert any(set(i) == set(j) for j in actual)
