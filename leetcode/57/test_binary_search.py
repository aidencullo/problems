import pytest

from interval import Interval
from binary_search import binary_search

@pytest.mark.binary
class TestBinary:

    @pytest.mark.parametrize(
        ('test_input', 'expected'),
        [
            (([[1, 3], [6, 9], [10, 11]], [1, 2]), 0),
            (([[1, 3], [6, 9],], [1, 2]), 0),
            (([[1, 3],], [1, 2]), 0),
            (([[1, 3], [6, 9], [10, 11]], [1, 4]), 1),
            (([[1, 3], [6, 9], [10, 11]], [6, 10]), 2),
            (([[1, 3], [6, 9], [10, 11]], [6, 8]), 1),
        ],
    )
    def test_binary_search_with_intervals(self, test_input, expected):
        assert binary_search(*test_input) == expected
