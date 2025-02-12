import pytest

from solution import MyStack

@pytest.fixture()
def s():
    return MyStack()


def testempty(s):
    assert s.empty()


def testPush(s):
    s.push(1)
    s.push(1)

    assert not s.empty()


def testPop(s):
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def testLeet(s):
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    assert s.pop() == 4
    s.push(5)
    assert s.pop() == 5
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
