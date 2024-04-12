import pytest
from LL import LinkedList

@pytest.fixture
def empty_linked_list():
    return LinkedList()

@pytest.fixture
def linked_list_with_data():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    return ll

def test_insert(empty_linked_list):
    empty_linked_list.insert(1)
    assert empty_linked_list.head.data == 1

def test_delete(linked_list_with_data):
    linked_list_with_data.delete(2)
    assert linked_list_with_data.head.data == 3
    assert linked_list_with_data.head.next.data == 1

def test_delete_head(linked_list_with_data):
    linked_list_with_data.delete(3)
    assert linked_list_with_data.head.data == 2

def test_delete_tail(linked_list_with_data):
    linked_list_with_data.delete(1)
    assert linked_list_with_data.head.data == 3
    assert linked_list_with_data.head.next.data == 2

def test_delete_not_found(linked_list_with_data):
    linked_list_with_data.delete(4)
    assert linked_list_with_data.head.data == 3
    assert linked_list_with_data.head.next.data == 2
    assert linked_list_with_data.head.next.next.data == 1
