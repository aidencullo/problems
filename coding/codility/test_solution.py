import pytest
from smallest_missing import solution

def test_example_1():
    A = [1, 3, 6, 4, 1, 2]
    assert solution(A) == 5

def test_example_2():
    A = [1, 2, 3]
    assert solution(A) == 4

def test_example_3():
    A = [-1, -3]
    assert solution(A) == 1

def test_single_element():
    A = [5]
    assert solution(A) == 1

def test_all_negative():
    A = [-1, -2, -3]
    assert solution(A) == 1

def test_all_positive():
    A = [1, 2, 3, 4]
    assert solution(A) == 5

def test_duplicates():
    A = [1, 1, 1, 1]
    assert solution(A) == 2

def test_large_range():
    A = list(range(1, 100001))  # Array from 1 to 100000
    assert solution(A) == 100001

def test_large_negative_range():
    A = list(range(-1000000, 0))  # Array from -1000000 to -1
    assert solution(A) == 1

def test_large_mix_range():
    A = list(range(-1000000, 1000001, 10000))  # Array with gaps
    assert solution(A) == 1

