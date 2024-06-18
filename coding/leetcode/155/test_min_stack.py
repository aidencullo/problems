import pytest
from min_stack import MinStack

@pytest.fixture
def stack():
    return MinStack()

def test_push(stack):
    stack.push(5)
    assert stack.top() == 5

def test_top_empty(stack):
    assert stack.top() == None

def test_getMin(stack):
    stack.push(5)
    stack.push(3)
    stack.push(7)
    assert stack.getMin() == 3

def test_getMin_duplicate_min(stack):
    stack.push(5)
    stack.push(3)
    stack.push(3)
    assert stack.getMin() == 3

def test_pop_min_update(stack):
    stack.push(5)
    stack.push(3)
    stack.pop()
    assert stack.getMin() == 5

def test_pop_empty(stack):
    with pytest.raises(IndexError):
        stack.pop()

def test_top_empty(stack):
    with pytest.raises(IndexError):
        stack.top()
