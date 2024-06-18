import pytest

from solution import MyQueue

@pytest.fixture()
def q():
    return MyQueue()


def testempty(q):
    assert q.empty()


def testPush(q):
    q.push(1)
    q.push(1)
    q.push(1)

    assert not q.empty()


def testPop(q):
    q.push(1)
    q.push(2)

    assert q.pop() == 1
    assert q.pop() == 2


def testQueueSimple(q):
    q = MyQueue()

    q.push(1)

    assert not q.empty()
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty()
    assert q.empty()


def testQueueComplex(q):
    q = MyQueue()

    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    assert not q.empty()
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.peek() == 3
    assert not q.empty()
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.empty()

def testLeet(q):

    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    assert q.pop() == 1
    q.push(5)
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5
