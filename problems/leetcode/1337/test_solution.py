import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([[1, 1, 0, 0, 0],
      [1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [1, 1, 1, 1, 1]], 3), [2, 0, 3]),
    (([[1, 0, 0, 0],
      [1, 1, 1, 1],
      [1, 0, 0, 0],
      [1, 0, 0, 0]], 2), [0, 2]),
])
def test_solution(test_input, expected):
    assert Solution().kWeakestRows(*test_input) == expected
