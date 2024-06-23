import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]],), Node(True, True, Node(True, True, None, None, None, None), Node(True, True, None, None, None, None), Node(True, True, None, None, None, None), Node(True, True, None, None, None, None))),

                (([[0,1],[1,0]],), Node(False, False, Node(True, True, None, None, None, None), Node(True, True, None, None, None, None), Node(True, True, None, None, None, None), Node(False, True, None, None, None, None))),

    ],
)
def test_solution(test_input, expected):
    assert Solution().construct(*test_input) == expected
