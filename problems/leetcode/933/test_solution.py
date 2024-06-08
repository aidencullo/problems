from solution import MyHashSet


def test_hashset_1():
    hashset = MyHashSet()
    hashset.add(1)
    assert hashset.contains(1)


def test_hashset_2():
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    assert hashset.contains(1)

def test_hashset_3():
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    hashset.add(3)
    hashset.add(4)
    hashset.add(5)
    hashset.add(6)
    assert hashset.contains(1)

def test_hashset_4():
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    hashset.add(3)
    hashset.add(4)
    hashset.add(5)
    hashset.add(6)
    assert hashset.contains(1)
    assert not hashset.contains(7)
    assert not hashset.contains(8)
    assert hashset.contains(6)
    assert hashset.contains(5)
    assert hashset.contains(4)
    assert hashset.contains(3)


def test_hashset_5():
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    hashset.remove(1)
    assert not hashset.contains(1)
    assert hashset.contains(2)
