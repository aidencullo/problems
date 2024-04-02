import pytest

from solution import max_collection

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (([5, 625, 4, 2, 5, 25],), 3),
        (([4, 7, 4, 8, 9],), -1),        
    ],
)
def test(test_input, expected):
    assert max_collection(*test_input) == expected
