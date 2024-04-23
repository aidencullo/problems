import pytest
from priority_queue import PriorityQueue

@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_enqueue_dequeue(priority_queue):
    priority_queue.enqueue('A', 5)
    priority_queue.enqueue('B', 1)
    priority_queue.enqueue('C', 2)
    priority_queue.enqueue('D', 0)
    assert priority_queue.dequeue() == 'A'
    assert priority_queue.dequeue() == 'C'
    assert priority_queue.dequeue() == 'B'

def test_dequeue_empty_queue(priority_queue):
    with pytest.raises(IndexError):
        priority_queue.dequeue()

def test_is_empty(priority_queue):
    assert priority_queue.is_empty() == True
    priority_queue.enqueue('A', 1)
    assert priority_queue.is_empty() == False

def test_size(priority_queue):
    assert priority_queue.size() == 0
    priority_queue.enqueue('A', 1)
    priority_queue.enqueue('A', 2)
    assert priority_queue.size() == 2


def test_equal_priority(priority_queue):
    priority_queue.enqueue('A', 3)
    priority_queue.enqueue('B', 3)
    assert priority_queue.dequeue() == 'A'
    assert priority_queue.dequeue() == 'B'


def test_equal_priority_2(priority_queue):
    priority_queue.enqueue('A', 3)
    priority_queue.enqueue('B', 3)
    priority_queue.enqueue('C', 3)
    priority_queue.enqueue('D', 5)
    priority_queue.enqueue('E', 1)
    priority_queue.enqueue('Z', 3)
    assert priority_queue.dequeue() == 'D'
    assert priority_queue.dequeue() == 'A'
    assert priority_queue.dequeue() == 'B'
    assert priority_queue.dequeue() == 'C'
    assert priority_queue.dequeue() == 'Z'
    assert priority_queue.dequeue() == 'E'
