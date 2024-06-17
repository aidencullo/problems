import pytest
from solution import Solution

# Create a fixture for the Solution class
@pytest.fixture
def solution_instance():
    return Solution()

# Test cases for flipAndInvertImage function
def test_flipAndInvertImage_example1(solution_instance):
    image = [[1,1,0],[1,0,1],[0,0,0]]
    expected_output = [[1,0,0],[0,1,0],[1,1,1]]
    assert solution_instance.flipAndInvertImage(image) == expected_output

def test_flipAndInvertImage_example2(solution_instance):
    image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    expected_output = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    assert solution_instance.flipAndInvertImage(image) == expected_output
