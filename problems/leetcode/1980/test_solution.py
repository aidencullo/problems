import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((["01","10"],), ["00","11"], ),
        ((["00","01"],), ["10","11"], ),
        ((["111","011","001"],), ["000", "010"], ),
    ],
)
def test_solution(test_input, expected):
    assert Solution().findDifferentBinaryString(*test_input) in expected
