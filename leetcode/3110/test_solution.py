import pytest


from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example1(solution):
    assert solution.scoreOfString("hello") == 13

def test_example2(solution):
    assert solution.scoreOfString("zaz") == 50

def test_custom1(solution):
    assert solution.scoreOfString("abc") == 6

def test_custom2(solution):
    assert solution.scoreOfString("xyz") == 6

# Add more test cases as needed
