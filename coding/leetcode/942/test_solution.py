import pytest

from solution import Solution

@pytest.fixture
def setup():
    return Solution()

def test_diStringMatch(setup):
    sol = setup

    assert sol.diStringMatch("IDID") == [0, 4, 1, 3, 2]
    assert sol.diStringMatch("III") == [0, 1, 2, 3]
    assert sol.diStringMatch("DDI") == [3, 2, 0, 1]

    # Add more test cases as needed
    assert sol.diStringMatch("DDIIDDI") == [6, 1, 5, 0, 4, 2, 3]
    assert sol.diStringMatch("IIDDIID") == [0, 2, 1, 6, 3, 5, 4]
    assert sol.diStringMatch("D") == [1, 0]
    assert sol.diStringMatch("I") == [0, 1]
