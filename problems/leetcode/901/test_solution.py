import pytest

from solution import StockSpanner


def test_solution():
    s = StockSpanner()
    assert s.next(100) == 1
    assert s.next(80) == 1
    assert s.next(60) == 1
    assert s.next(70) == 2
    assert s.next(60) == 1
    assert s.next(75) == 4
    assert s.next(85) == 6

def test_other():
    s = StockSpanner()
    assert s.next(29) == 1
    assert s.next(91) == 2
    assert s.next(62) == 1
    assert s.next(76) == 2
    assert s.next(51) == 1

def test_other_2():
    s = StockSpanner()
    assert s.next(28) == 1
    assert s.next(14) == 1
    assert s.next(28) == 3
    assert s.next(35) == 4
    assert s.next(46) == 5
    assert s.next(53) == 6
    assert s.next(66) == 7
    assert s.next(80) == 8
    assert s.next(87) == 9
    assert s.next(88) == 10

def test_time_limit():
    s = StockSpanner()
    for i in range(1, 10000):
        assert s.next(i) == i
