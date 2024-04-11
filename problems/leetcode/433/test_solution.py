import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('AACCGGTT', 'AACCGGTA', ['AACCGGTA']), 1),
        (('AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']), 2),
        (('AAAAACCC', 'AACCCCCC', ['AAAACCCC', 'AAACCCCC', 'AACCCCCC']), 3),
        (("AACCGGTT", "AACCGGTA", []), -1),
        (("AACCGGTT", "AACCGCTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]), 2),
    ]
)
def testSolution(test_input, expected):
    sol = Solution()
    assert sol.minMutation(*test_input) == expected
