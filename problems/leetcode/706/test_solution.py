from solution import MyHashMap

def test_put_get_remove():
    my_hash_map = MyHashMap()

    # Test put and get
    my_hash_map.put(1, 10)
    assert my_hash_map.get(1) == 10

    # Test overwrite
    my_hash_map.put(1, 20)
    assert my_hash_map.get(1) == 20

    # Test remove
    my_hash_map.remove(1)
    assert my_hash_map.get(1) == -1

def test_non_existent_key():
    my_hash_map = MyHashMap()

    # Test getting non-existent key
    assert my_hash_map.get(2) == -1

def test_empty_hash_map():
    my_hash_map = MyHashMap()

    # Test removing from empty hash map
    my_hash_map.remove(1)  # Should not raise any error

def test_put_remove():
    my_hash_map = MyHashMap()

    # Test putting and then removing
    my_hash_map.put(1, 10)
    my_hash_map.remove(1)
    assert my_hash_map.get(1) == -1

def test_contains():
    my_hash_map = MyHashMap()

    # Test contains
    my_hash_map.put(1, 10)
    assert my_hash_map.contains(1) == True
    assert my_hash_map.contains(2) == False


# Additional test cases
def test_put_multiple():
    my_hash_map = MyHashMap()

    # Test putting multiple keys
    my_hash_map.put(1, 10)
    my_hash_map.put(2, 20)
    my_hash_map.put(3, 30)
    assert my_hash_map.get(1) == 10
    assert my_hash_map.get(2) == 20
    assert my_hash_map.get(3) == 30

def test_remove_multiple():
    my_hash_map = MyHashMap()

    # Test removing multiple keys
    my_hash_map.put(1, 10)
    my_hash_map.put(2, 20)
    my_hash_map.put(3, 30)
    my_hash_map.remove(1)
    my_hash_map.remove(2)
    my_hash_map.remove(3)
    assert my_hash_map.get(1) == -1
    assert my_hash_map.get(2) == -1
    assert my_hash_map.get(3) == -1


def test_contains_multiple():
    my_hash_map = MyHashMap()

    # Test contains for multiple keys
    my_hash_map.put(1, 10)
    my_hash_map.put(2, 20)
    my_hash_map.put(3, 30)
    assert my_hash_map.contains(1) == True
    assert my_hash_map.contains(2) == True
    assert my_hash_map.contains(3) == True
    assert my_hash_map.contains(4) == False
    assert my_hash_map.contains(5) == False
    assert my_hash_map.contains(6) == False

def test_constraints():
    my_hash_map = MyHashMap()
    for i in range(10 ** 4):
        my_hash_map.put(i, i)
    for i in range(10 ** 4):
        my_hash_map.put(i, i * 2)
    for i in range(10 ** 4):
        assert my_hash_map.get(i) == i * 2
    for i in range(10 ** 4):
        my_hash_map.remove(i)
        assert my_hash_map.get(i) == -1
