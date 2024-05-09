import pytest

from mergesort import mergesort


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5],),
        ([2, 1, 3, 5, 4], [1, 2, 3, 4, 5],),
        ([2, 3, 5, 1, 4], [1, 2, 3, 4, 5],),
        ([3, 5, 2, 1, 4], [1, 2, 3, 4, 5],),
        ([3, 5, 2, 1], [1, 2, 3, 5],),
        ([2, 1], [1, 2],),
        ([1], [1],),
    ],
)
def test_mergesort(test_input, expected):
    assert mergesort(test_input) == expected
