import pytest
from solution import MyCircularQueue


def test_solution():
    myCircularQueue = MyCircularQueue(3)
    assert myCircularQueue.enQueue(1)
    assert myCircularQueue.enQueue(2)
    assert myCircularQueue.enQueue(3)
    assert not myCircularQueue.enQueue(4)
    assert myCircularQueue.Rear() == 3
    assert myCircularQueue.isFull()
    assert myCircularQueue.deQueue()
    assert myCircularQueue.enQueue(4)
    assert myCircularQueue.Rear() == 4


def test_Leetcode():
    q = MyCircularQueue(6)
    assert q.enQueue(6)
    assert q.Rear() == 6
    assert q.deQueue()
    assert q.enQueue(5)
    assert q.Rear() == 5
    assert q.deQueue()
    assert q.Front() == -1
    assert not q.deQueue()
    assert not q.deQueue()
    assert not q.deQueue()

'''
["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"]
[[6],[6],[],[],[],[5],[],[],[],[],[],[]]
'''
