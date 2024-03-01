import pytest

from binary_search import binary_search


class TestBinarySearch:

    @pytest.mark.parametrize(
        ('test_input', 'expected'),
        [
            (([1,2,3,4,5,6], 7), 5),
            (([1,2,4,5,6], 7), 4),
            (([1,2,4,5,6], 2), 1),
            (([1,2,4,5,6], 4), 2),
            ((list(range(10)), 4), 4),
            ((list(range(10)), 5), 5),
        ]
    )
    def test_binary_search(self, test_input, expected):
        assert binary_search(*test_input) == expected
