from solution import MyHashSet


def test_hashset():
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    assert hashset.contains(1)
    assert not hashset.contains(3)
    hashset.add(2)
    assert hashset.contains(2)
    hashset.remove(2)
    assert not hashset.contains(2)


def test_hashset_2():
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    hashset.add(3)
    hashset.add(4)
    hashset.add(5)
    hashset.add(6)
    hashset.add(7)
    hashset.add(8)
    hashset.remove(8)
    hashset.remove(7)
    hashset.remove(6)
    hashset.remove(4)
    hashset.remove(3)
    hashset.remove(2)
    hashset.add(1000000)
    assert hashset.contains(1)
    hashset.add(1000000)
    assert hashset.contains(1)
    hashset.add(1000000)
    assert hashset.contains(1)
    hashset.add(1000000)
    assert hashset.contains(1)
    assert not hashset.contains(2)
    assert not hashset.contains(3)
    assert not hashset.contains(4)
    assert not hashset.contains(6)
    assert not hashset.contains(7)
    hashset.add(8457023948573290854793054)
    hashset.add(938429034928349039393993939)
    assert hashset.contains(1)
