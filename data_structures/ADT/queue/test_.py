import pytest
from priority_queue import PriorityQueue

@pytest.fixture
def priority_queue():
    return PriorityQueue()

def test_enqueue_dequeue(priority_queue):
    priority_queue.enqueue('task1', 3)
    priority_queue.enqueue('task2', 1)
    priority_queue.enqueue('task3', 2)
    assert priority_queue.dequeue() == 'task1'
    assert priority_queue.dequeue() == 'task3'
    assert priority_queue.dequeue() == 'task2'

def test_dequeue_empty_queue(priority_queue):
    with pytest.raises(IndexError):
        priority_queue.dequeue()

def test_is_empty(priority_queue):
    assert priority_queue.is_empty() == True
    priority_queue.enqueue('task', 1)
    assert priority_queue.is_empty() == False

def test_size(priority_queue):
    assert priority_queue.size() == 0
    priority_queue.enqueue('task1', 1)
    priority_queue.enqueue('task2', 2)
    assert priority_queue.size() == 2


def test_equal_priority(priority_queue):
    priority_queue.enqueue('task1', 3)
    priority_queue.enqueue('task3', 3)
    assert priority_queue.dequeue() == 'task1'
    assert priority_queue.dequeue() == 'task3'   
