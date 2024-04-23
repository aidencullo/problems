import pytest

from heap import MinHeap

def test_heap_insert():
    h = MinHeap()
    h.insert(5)
    h.insert(3)
    h.insert(4)
    h.insert(1)
    h.insert(2)
    h.insert(7)
    h.insert(6)

    assert h.extract_min() == 1
    assert h.extract_min() == 2
    assert h.extract_min() == 3
    assert h.extract_min() == 4
    assert h.extract_min() == 5
    assert h.extract_min() == 6
    assert h.extract_min() == 7
    assert h.is_empty()


def test_heap_delete():
    h = MinHeap()
    h.insert(5)
    h.insert(3)
    h.insert(4)
    h.insert(1)
    h.insert(2)
    h.insert(7)
    h.insert(6)
    h.delete(5)
    h.delete(3)
    h.delete(4)

    assert h.extract_min() == 1
    assert h.extract_min() == 2
    assert h.extract_min() == 6
    assert h.extract_min() == 7
    assert h.is_empty()

    
def test_heap_get_min():
    h = MinHeap()
    h.insert(5)
    h.insert(3)
    h.insert(4)
    h.insert(1)
    h.insert(2)
    h.insert(7)
    h.insert(6)
    h.delete(5)

    assert h.get_min() == 1
    assert h.get_min() == 1
    h.delete(1)
    assert h.get_min() == 2

def test_heap_negative():
    h = MinHeap()
    h.insert(0)
    assert h.get_min() == 0
    h.insert(1)
    assert h.get_min() == 0
    h.insert(2)
    assert h.get_min() == 0
    h.insert(-3)
    assert h.get_min() == -3
    h.delete(-3)
    assert h.get_min() == 0
    h.delete(0)
    assert h.get_min() == 1

   
def test_heapify_1():
    h = MinHeap()
    h.insert(5)
    h.delete(5)
    assert h.is_empty()    

      
def test_heapify_2():
    h = MinHeap()
    h.insert(5)
    h.insert(1)
    h.delete(5)
    assert h.get_min() == 1

def test_heapify_3():
    h = MinHeap()
    h.insert(5)
    h.insert(1)
    h.delete(1)
    assert h.get_min() == 5
    h.delete(5)


def test_heapify_100():
    h = MinHeap()
    for i in range(-100, 100):
        h.insert(i)
    for i in range(-100, 100):
        assert h.get_min() == i
        h.delete(i)
    assert h.is_empty()

def test_heapify_hackerrank():
    h = MinHeap()
    h.insert(10)
    h.insert(9)
    assert h.get_min() == 9
    h.insert(3)
    assert h.get_min() == 3
    h.delete(9)
    assert h.get_min() == 3
    h.delete(3)
    assert h.get_min() == 10
    h.insert(5)
    h.insert(2)
    assert h.get_min() == 2
