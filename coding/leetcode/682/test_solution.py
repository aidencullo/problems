# tests/test_solution.py
import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_example1(solution):
    operations = ["5", "2", "C", "D", "+"]
    assert solution.calPoints(operations) == 30

def test_example2(solution):
    operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    assert solution.calPoints(operations) == 27

def test_example3(solution):
    operations = ["1", "C"]
    assert solution.calPoints(operations) == 0

def test_custom_example1(solution):
    operations = ["10", "20", "+", "D", "C", "15"]
    assert solution.calPoints(operations) == 75

def test_custom_example2(solution):
    operations = ["8", "9", "D", "C", "7", "+"]
    assert solution.calPoints(operations) == 48
