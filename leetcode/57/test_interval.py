import pytest

from interval import Interval

@pytest.mark.interval
class TestExample:

    @pytest.mark.parametrize(
        ('test_input', 'expected'),
        [
            (([1,2], [2,3]), True),
            (([1,3], [1,4]), True),
            (([1,2], [2,30]), True),
            (([1,10], [2,3]), True),
            (([5,10], [2,3]), False),
        ],
    )
    def test_example(self, test_input, expected):
        i1, i2 = test_input
        assert (Interval(*i1) < Interval(*i2)) == expected
