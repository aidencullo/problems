import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([4, 3, 2, 3, 5, 2, 1], 4), True),
        (([1, 2, 3, 4], 3), False),
        (([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 5), True), (([7628,3147,7137,2578,7742,2746,4264,7704,9532,9679,8963,3223,2133,7792,5911,3979], 6), False),
    ]
)
def testSolution(test_input, expected):
    assert Solution().canPartitionKSubsets(*test_input) == expected
