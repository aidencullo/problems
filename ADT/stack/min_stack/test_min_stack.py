import pytest
from minstack import MinStack

@pytest.fixture
def empty_stack():
    return MinStack()

@pytest.fixture
def filled_stack():
    stack = MinStack()
    stack.push(5)
    stack.push(3)
    stack.push(7)
    stack.push(2)
    stack.push(6)
    return stack

def test_empty_stack(empty_stack):
    assert empty_stack.top() is None
    assert empty_stack.get_min() is None
    assert empty_stack.pop() is None

def test_filled_stack(filled_stack):
    assert filled_stack.top() == 6
    assert filled_stack.get_min() == 2
    assert filled_stack.pop() == 6
    assert filled_stack.top() == 2
    assert filled_stack.get_min() == 2
    filled_stack.pop()
    filled_stack.pop()
    assert filled_stack.get_min() == 3
    assert filled_stack.top() == 3
    filled_stack.pop()
    assert filled_stack.get_min() == 5
    assert filled_stack.top() == 5
    filled_stack.pop()
    assert filled_stack.get_min() is None
    assert filled_stack.top() is None
    assert filled_stack.pop() is None

def test_push_and_pop(empty_stack):
    empty_stack.push(10)
    assert empty_stack.top() == 10
    assert empty_stack.get_min() == 10
    empty_stack.push(5)
    assert empty_stack.top() == 5
    assert empty_stack.get_min() == 5
    empty_stack.push(15)
    assert empty_stack.top() == 15
    assert empty_stack.get_min() == 5
    empty_stack.pop()
    assert empty_stack.top() == 5
    assert empty_stack.get_min() == 5
    empty_stack.pop()
    assert empty_stack.top() == 10
    assert empty_stack.get_min() == 10
    empty_stack.pop()
    assert empty_stack.top() is None
    assert empty_stack.get_min() is None
    assert empty_stack.pop() is None
