class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        # insert a node at beginning with both next and prev references
        self.head = Node(value, self.head)

    def includes(self, key):
        # apples -> bananas -> cherries -> None; key = oranges
        current = self.head
        while current is not None:
            if current.value == key:
                return True
            current = current.next

        return False


class Node:
    def __init__(self, value, next=None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev