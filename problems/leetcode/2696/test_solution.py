# test_solution.py

import pytest
from solution import Solution

def test_min_length_case1():
    sol = Solution()
    assert sol.minLength("ABFCACDB") == 2

def test_min_length_case2():
    sol = Solution()
    assert sol.minLength("ACBBD") == 5

def test_min_length_no_operations():
    sol = Solution()
    assert sol.minLength("XYZ") == 3

def test_min_length_single_removal():
    sol = Solution()
    assert sol.minLength("ACBD") == 4

def test_min_length_nested_removals():
    sol = Solution()
    assert sol.minLength("CABDCABABCD") == 1

def test_min_length_mixed_case():
    sol = Solution()
    assert sol.minLength("AABBCCDD") == 0

def test_min_length_alternating():
    sol = Solution()
    assert sol.minLength("ABCDABCD") == 0
