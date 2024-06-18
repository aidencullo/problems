from collections import deque

class Stack:

    def __init__(self):
        self.items = deque()

    def __repr__(self):
        return repr(self.items)

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

NUMBERS_INPUT = [
    (1,),
    (0,),
    (10000,),
    (-1,),
]



## PUSH

@pytest.mark.parametrize(
    ('test_input'),
    NUMBERS_INPUT,
)
def test_push_once(test_input, stack_mock):
    stack_mock.push(test_input)
    assert test_input == stack_mock.pop()


@pytest.mark.parametrize(
    ('test_input'),
    NUMBERS_INPUT,
)
def test_push_multiple(test_input, stack_mock):
    stack_mock.push(test_input)
    stack_mock.push(test_input * 2)
    assert test_input * 2 == stack_mock.pop()
    assert test_input == stack_mock.pop()

## POP

def test_pop_on_empty(stack_mock):
    with pytest.raises(IndexError):
        stack_mock.pop()


@pytest.mark.parametrize(
    ('test_input'),
    NUMBERS_INPUT,
)
def test_pop_on_full(test_input, stack_mock):
    stack_mock.push(test_input)
    assert test_input == stack_mock.pop()

@pytest.mark.parametrize(
    ('test_input'),
    NUMBERS_INPUT,
)
def test_pop_on_multiple_pushes(test_input, stack_mock):
    stack_mock.push(test_input * 3)
    stack_mock.push(test_input)
    stack_mock.pop()
    assert test_input * 3 == stack_mock.pop()




## PEEK

@pytest.mark.parametrize(
    ('test_input'),
    NUMBERS_INPUT,
)
def test_peek_on_fully(test_input, stack_mock):
    stack_mock.push(test_input)
    assert test_input == stack_mock.peek()
    assert test_input == stack_mock.peek()
    

@pytest.mark.parametrize(
    ('test_input'),
    NUMBERS_INPUT,
)
def test_peek_on_multiple_pops(test_input, stack_mock):
    stack_mock.push(test_input * 3)
    stack_mock.push(test_input)
    stack_mock.pop()
    assert test_input * 3 == stack_mock.peek()


def test_peek_on_empty(stack_mock):
    with pytest.raises(Exception):
        stack_mock.peek()



## IS_EMPTY

def test_is_empty():
    assert stack_mock.isEmpty()


@pytest.mark.parametrize(
    ('test_input'),
    NUMBERS_INPUT,
)
def test_is_empty(test_input, stack_mock):
    stack_mock.push(test_input)
    assert not stack_mock.isEmpty()


@pytest.mark.parametrize(
    ('test_input'),
    NUMBERS_INPUT,
)
def test_is_empty(test_input, stack_mock):
    stack_mock.push(test_input)
    stack_mock.pop()
    assert stack_mock.isEmpty()
