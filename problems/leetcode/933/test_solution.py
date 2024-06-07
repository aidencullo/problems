# import pytest

# from solution import Solution


# @pytest.mark.parametrize("test_input, expected", [
#     (([3,1,2,4],), [2,4,3,1]),
#     (([0],), [0]),
# ])
# def test_solution(test_input, expected):
#     assert Solution().sortArrayByParity(*test_input) == expected

import pytest

from solution import RecentCounter


def test_recenter_counter():
    rc = RecentCounter()
    assert rc.ping(1) == 1
    assert rc.ping(100) == 2
    assert rc.ping(3001) == 3
    assert rc.ping(3002) == 3
