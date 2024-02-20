import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]]),
        (([[0,0,0],[0,0,0],], 0, 0, 0), [[0,0,0],[0,0,0],]),
        (([[0,0,0],[0,0,0],], 1, 1, 0), [[0,0,0],[0,0,0],]),
        (([[0,0,0],[0,0,0],], 0, 0, 1), [[1,1,1],[1,1,1],]),
        (([[0,0,0],[0,0,0],], 0, 1, 1), [[1,1,1],[1,1,1],]),
        (([[0,0,0],[0,1,0],], 1, 1, 2), [[0,0,0],[0,2,0]],),
        
    ],
)
def test_(test_input, expected):
    # Act
    result = Solution().floodFill(*test_input)

    # Assert    
    assert result == expected
