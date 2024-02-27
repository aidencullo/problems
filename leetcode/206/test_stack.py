import pytest

from stack import Stack


def test_stack_1():
    s = Stack()
    assert not s
    s.push(1)
    assert s


def test_stack_3():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
