class Stack:

    def __init__(self):
        self.items = []
    
    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.isEmpty():
            raise Exception('stack is empty')
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0



import pytest
from unittest.mock import Mock

@pytest.fixture(name="stack_mock")
def fixture():
    return Stack()
    return Mock()


@pytest.mark.parametrize(
    ('test_input'),
    [
        (4,),
        (5,),
        (0,),
        (10000,),
        (-1,),
    ],
)
def test_push_once(test_input, stack_mock):
    stack_mock.push(test_input)
    assert test_input == stack_mock.pop()

@pytest.mark.parametrize(
    ('test_input'),
    [
        (4,),
        (5,),
        (0,),
        (10000,),
        (-1,),
    ],
)
def test_push_multiple(test_input, stack_mock):
    stack_mock.push(test_input)
    stack_mock.push(test_input)
    stack_mock.push(test_input)
    stack_mock.push(test_input)
    stack_mock.push(test_input)
    assert test_input == stack_mock.pop()
    assert test_input == stack_mock.pop()
    assert test_input == stack_mock.pop()

def test_pop_on_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


@pytest.mark.parametrize(
    ('test_input'),
    [
        (4,),
        (5,),
        (0,),
        (10000,),
        (-1,),
    ],
)
def test_peek_on_fully(test_input, stack_mock):
    stack_mock.push(test_input)
    assert test_input == stack_mock.peek()
    assert test_input == stack_mock.peek()
 
@pytest.mark.parametrize(
    ('test_input'),
    [
        (4,),
        (5,),
        (0,),
        (10000,),
        (-1,),
    ],
)
def test_peek_on_multiple_pops(test_input, stack_mock):
    stack_mock.push(test_input * 3)
    stack_mock.push(test_input)
    assert test_input == stack_mock.peek()
    stack_mock.pop()
    assert test_input * 3 == stack_mock.peek()

def test_peek_on_empty():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()

@pytest.mark.parametrize(
    ('test_input'),
    [
        (4,),
        (0,),
        (10000,),
    ],
)
def test_is_empty(test_input, stack_mock):
    assert stack_mock.isEmpty()
    stack_mock.push(test_input)
    assert not stack_mock.isEmpty()
    stack_mock.pop()
    assert stack_mock.isEmpty()
    assert stack_mock.isEmpty()
