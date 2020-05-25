import pytest

from linked_list.doubly_linked_list import DoublyLinkedList, Node


def test_create_doubly_linked_list():
    l = DoublyLinkedList()


def test_node():
    node = Node("apple")
    assert node.value == "apple"
    assert node.next == None
    assert node.prev == None


def test_linked_list_nodes():
    fruits = DoublyLinkedList()
    fruits.head = Node("apples")
    fruits.head.next = Node("bananas")

    assert fruits.head.next.value == "bananas"


def test_insert_to_empty_list():
    fruits = DoublyLinkedList()
    fruits.insert("apples")

    assert fruits.head.value == "apples"
    assert fruits.head.next == None


def test_insert_to_nonempty_list():
    fruits = DoublyLinkedList()
    fruits.insert("apples")
    fruits.insert("bananas")
    assert fruits.head.value == "bananas"
    assert fruits.head.next.value == "apples"


def test_insert_more(some_doubly_linked_list):
    some_doubly_linked_list.insert("oranges")


def test_includes(some_doubly_linked_list):
    assert some_doubly_linked_list.includes("apples")
    assert some_doubly_linked_list.includes("bananas")
    assert some_doubly_linked_list.includes("cherries")


def test_includes_false(some_doubly_linked_list):
    assert some_doubly_linked_list.includes("oranges") == False


@pytest.fixture
def some_doubly_linked_list():
    # "{ cherries } -> <- { bananas } -> <-{ apples } -> NULL"
    fruits = DoublyLinkedList()
    fruits.insert("apples")
    fruits.insert("bananas")
    fruits.head.next.prev = fruits.head
    fruits.insert("cherries")
    fruits.head.next.prev = fruits.head
    return fruits