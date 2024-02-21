import pytest

from util import Stack

def testStackEmpty():
    # Arrange
    s = Stack()

    # Act
    
    # Arrange
    assert s.isEmpty()

def testStackOneItem():
    # Arrange
    s = Stack()

    # Act
    s.push(1)
    
    # Arrange
    assert not s.isEmpty()
    assert s.peek() == 1
    assert s.pop() == 1
    assert s.isEmpty()


def testStackTenItem():
    # Arrange
    s = Stack()

    # Act
    for i in range(10):
        s.push(i)
    
    # Assert
    assert not s.isEmpty()
    for i in range(10)[::-1]:
        assert s.peek() == i
        assert s.pop() == i
    assert s.isEmpty()
