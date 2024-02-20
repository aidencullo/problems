import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([-1,0,3,5,9,12], 9), 4),
        (([-1,0,3,5,7,9,12], 9), 5),
        (([-1,0,9,12], 9), 2),
        (([9], 9), 0),
        (([1,9], 9), 1),
        (([1,9], 2), -1),
        (([1,9], 6), -1),
        (([1,9], -1), -1),
        (([1,4,5,8,9], -1), -1),
    ],
)
def test_(test_input, expected):
    # Act
    result = Solution().search(*test_input)

    # Assert    
    assert result == expected
