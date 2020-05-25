import pytest

from linked_list import __version__
from linked_list.linked_list import LinkedList, Node


def test_version():
    assert __version__ == '0.1.0'


def test_linked_list_creation():
    l1 = LinkedList()


def test_node():
    node = Node("apple")
    assert node.value == "apple"
    assert node.next == None


def test_linked_list_nodes():
    fruits = LinkedList()
    fruits.head = Node("apples")
    fruits.head.next = Node("bananas")

    assert fruits.head.next.value == "bananas"


def test_insert_to_empty_list():
    fruits = LinkedList()
    fruits.insert("apples")

    assert fruits.head.value == "apples"
    assert fruits.head.next == None


def test_insert_to_nonempty_list():
    fruits = LinkedList()
    fruits.insert("apples")
    fruits.insert("bananas")
    assert fruits.head.value == "bananas"
    assert fruits.head.next.value == "apples"


def test_insert_more(some_linked_list):
    assert some_linked_list.head.value == "cherries"
    assert some_linked_list.head.next.value == "bananas"
    assert some_linked_list.head.next.next.value == "apples"


def test_includes_true(some_linked_list):
    assert some_linked_list.includes("apples")
    assert some_linked_list.includes("bananas")
    assert some_linked_list.includes("cherries")


def test_includes_false(some_linked_list):
    assert some_linked_list.includes("oranges") == False


def test_str(some_linked_list):
    assert some_linked_list.__str__() == "{ cherries } -> { bananas } -> { apples } -> NULL"


# make the linkedlist a fixture to reduce repetition
@pytest.fixture
def some_linked_list():
    # "{ cherries } -> { bananas } -> { apples } -> NULL"
    fruits = LinkedList()
    fruits.insert("apples")
    fruits.insert("bananas")
    fruits.insert("cherries")
    return fruits
