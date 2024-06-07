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
