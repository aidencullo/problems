import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23),
        ([1,2], 3),
    ],
)
def testSolution(test_input, expected):
    # Arrange
    s = Solution()

    # Act
    actual = s.maxSubArray(test_input)
    
    # Assert
    assert actual == expected
