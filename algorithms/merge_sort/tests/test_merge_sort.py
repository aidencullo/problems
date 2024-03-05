import pytest

from src.merge_sort import merge_sort


test_data = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5],),
    ([2, 1, 3, 5, 4], [1, 2, 3, 4, 5],),
    ([2, 3, 5, 1, 4], [1, 2, 3, 4, 5],),
    ([3, 5, 2, 1, 4], [1, 2, 3, 4, 5],),
    ([3, 5, 2, 1], [1, 2, 3, 5],),
    ([2, 1], [1, 2],),
    ([1], [1],),
]


class TestMergeSort:

    @pytest.mark.parametrize(
        ('test_input', 'expected'),
        test_data,
    )
    def test_merge_sort(self, test_input, expected):
        assert merge_sort(test_input) == expected
