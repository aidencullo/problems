import pytest

from solution import MyQueue

def testIsEmpty():
    # Arrange
    q = MyQueue()

    # Assert
    assert q.isEmpty()

def testPush():
    # Arrange
    q = MyQueue()

    # Assert
    q.push(1)
    q.push(1)
    q.push(1)

    # Assert
    assert not q.isEmpty()

def testPop():
    # Arrange
    q = MyQueue()

    # Act
    # Assert
    q.push(1)
    q.push(2)
    assert not q.pop() == 1
    assert not q.isEmpty()
    assert not q.pop() == 2
    assert q.isEmpty()

def testQueueSimple():
    # Assert
    q = MyQueue()

    # Act
    # Assert    
    q.push(1)
    assert not q.isEmpty()
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.isEmpty()
    assert q.isEmpty()


def testQueueComplex():
    # Assert
    q = MyQueue()

    # Act
    # Assert    
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    assert not q.isEmpty()
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.peek() == 3
    assert not q.isEmpty()
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.isEmpty()
