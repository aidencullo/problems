from typing import List

import pytest

from solution import (getUniformIntegerCountInInterval,
                      uniformFromLeadingDigit, isUniform, findNextUniform)

# A = 75
# B = 300
# Expected Return Value = 5
# Sample test case #2
# A = 1
# B = 9
# Expected Return Value = 9
# Sample test case #3
# A = 999999999999
# B = 999999999999
# Expected Return Value = 1

test_data_getUniformIntegerCountInInterval: List[tuple[int, int, int]] = [
    (75, 300, 5),
]
@pytest.mark.parametrize("A, B, expected",
                         test_data_getUniformIntegerCountInInterval)
def test_getUniformIntegerCountInInterval(A: int, B: List[int], expected: int):
    # Assert
    assert getUniformIntegerCountInInterval(A, B) == expected





    
    
test_data_uniformFromLeadingDigit: List[tuple[int, int]] = [
    (75, 77),
    (76, 77),
    (77, 77),
    (7700, 7777),
    (10099, 11111),
]

@pytest.mark.parametrize("A, expected",
                         test_data_uniformFromLeadingDigit)
def test_uniformFromLeadingDigit(A: int, expected: int):
    # Assert
    assert uniformFromLeadingDigit(A) == expected






    
    
test_data_isUniform: List[tuple[int, bool]] = [
    (75, False),
    (77, True),
]

@pytest.mark.parametrize("A, expected",
                         test_data_isUniform)
def test_isUniform(A: int, expected: bool):
    # Assert
    assert isUniform(A) == expected

    



test_data_findNextUniform: List[tuple[int, int]] = [
    (75, 77),
    (77, 77),
    (79, 88),
    (179, 222),
]

@pytest.mark.parametrize("A, expected",
                         test_data_findNextUniform)
def test_findNextUniform(A: int, expected: int):
    # Assert
    assert findNextUniform(A) == expected

    
