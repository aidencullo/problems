from solution import MedianFinder

import pytest

@pytest.fixture
def median_finder():
    return MedianFinder()

def test_find_median(median_finder):
    median_finder.addNum(1)
    median_finder.addNum(2)
    assert median_finder.findMedian() == 1.5
    median_finder.addNum(3)
    assert median_finder.findMedian() == 2.0

def test_find_median_2(median_finder):
    median_finder.addNum(2)
    median_finder.addNum(3)
    median_finder.addNum(4)
    assert median_finder.findMedian() == 3.0
    median_finder.addNum(1)
    assert median_finder.findMedian() == 2.5

def test_find_median_3(median_finder):
    median_finder.addNum(1)
    median_finder.addNum(2)
    median_finder.addNum(3)
    median_finder.addNum(4)
    median_finder.addNum(5)
    assert median_finder.findMedian() == 3.0
    median_finder.addNum(6)
    assert median_finder.findMedian() == 3.5

def test_find_median_4(median_finder):
    median_finder.addNum(1)
    median_finder.addNum(2)
    median_finder.addNum(3)
    median_finder.addNum(4)
    median_finder.addNum(5)
    median_finder.addNum(6)
    assert median_finder.findMedian() == 3.5
    median_finder.addNum(7)
    assert median_finder.findMedian() == 4.0
    median_finder.addNum(8)
    assert median_finder.findMedian() == 4.5
