import pytest
from priority_queue import PriorityQueue

@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_enqueue_dequeue(priority_queue):
    priority_queue.enqueue(5)
    priority_queue.enqueue(1)
    priority_queue.enqueue(2)
    assert priority_queue.dequeue() == 5
    assert priority_queue.dequeue() == 2
    assert priority_queue.dequeue() == 1

def test_dequeue_empty_queue(priority_queue):
    with pytest.raises(IndexError):
        priority_queue.dequeue()

def test_is_empty(priority_queue):
    assert priority_queue.is_empty() == True
    priority_queue.enqueue(1)
    assert priority_queue.is_empty() == False

def test_size(priority_queue):
    assert priority_queue.size() == 0
    priority_queue.enqueue(1)
    priority_queue.enqueue(2)
    assert priority_queue.size() == 2


def test_equal_priority(priority_queue):
    priority_queue.enqueue(3)
    priority_queue.enqueue(3)
    assert priority_queue.dequeue() == 3
    assert priority_queue.dequeue() == 3
