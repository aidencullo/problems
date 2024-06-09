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
