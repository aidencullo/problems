import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([[1,3,2],[4,5,2],[2,4,3]],), 4),
    (([[1,3,2],[4,5,2],[1,5,5]],), 5),
    (([[1,5,3],[1,5,1],[6,6,5]],), 8),
    (([[10,83,53],[63,87,45],[97,100,32],[51,61,16]],), 93),
])
def test_solution(test_input, expected):
    assert Solution().maxTwoEvents(*test_input) == expected
