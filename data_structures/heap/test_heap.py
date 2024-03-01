import pytest

from heap import Heap

@pytest.fixture
def heap_fixture():
    return Heap()

@pytest.mark.heap
class TestHeap:

    def test_insert_single(self, heap_fixture):
        heap_fixture.insert(1)
        assert heap_fixture.root == 1


    def test_insert_single(self, heap_fixture):
        heap_fixture.insert(1)
        heap_fixture.insert(1)
        heap_fixture.insert(1)
        assert heap_fixture.root.left == 1
        assert heap_fixture.root.right == 1
