import pytest
from heap import MinHeap

@pytest.fixture
def empty_heap():
    return MinHeap()

@pytest.fixture
def filled_heap():
    heap = MinHeap()
    heap.push(5)
    heap.push(3)
    heap.push(7)
    heap.push(1)
    return heap

def test_push(empty_heap):
    empty_heap.push(5)
    assert empty_heap.peek() == 5

def test_pop(filled_heap):
    assert filled_heap.pop() == 1
    assert filled_heap.pop() == 3

def test_peek(filled_heap):
    assert filled_heap.peek() == 1

def test_empty_heap_pop(empty_heap):
    with pytest.raises(IndexError):
        empty_heap.pop()

def test_empty_heap_peek(empty_heap):
    assert empty_heap.peek() is None
