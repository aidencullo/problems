import pytest
from lrucache import LRUCache

@pytest.fixture
def cache():
    return LRUCache(2)  # Capacity of 2 for testing purposes

def test_cache_operations(cache):
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1

    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1

    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_cache_operations_simple():
    cache = LRUCache(1)
    cache.put(2, 1)
    assert cache.get(2) == 1

def test_cache_operations_eviction():
    cache = LRUCache(1)
    cache.put(2, 1)
    assert cache.get(2) == 1
    cache.put(3, 2)
    assert cache.get(2) == -1
    assert cache.get(3) == 2

def test_cache_operations_eviction_2():
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3
