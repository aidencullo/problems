import pytest

from solution import Solution
from util import buildCycleList

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        # (([3, 2, 0, -4], 1), True),
        (([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5], -1), False),
    ],
)
def testSolution(test_input, expected):
    # Assert
    ll_input = buildCycleList(*test_input)

    # Act
    result = Solution().hasCycle(ll_input)

    # Assert    
    assert result == expected

def testBuildListWithCycle():
    # Act
    ll_input = buildCycleList([1, 2, 3], pos=1)

    # Assert    
    assert ll_input.val == 1
    assert ll_input.next.val == 2
    assert ll_input.next.next.val == 3
    assert ll_input.next.next.next.val == 2


def testBuildListWithoutCycle():
    # Act
    ll_input = buildCycleList([1, 2, 3], pos=-1)

    # Assert    
    assert ll_input.val == 1
    assert ll_input.next.val == 2
    assert ll_input.next.next.val == 3
    assert ll_input.next.next.next == None
