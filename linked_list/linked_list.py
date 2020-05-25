class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, key):
        # apples -> bananas -> cherries -> None; key = oranges

        current = self.head
        while current is not None:
            if current.value == key:
                return True
            current = current.next
        return False

    def __str__(self):
        output_string = ""
        current = self.head
        while current is not None:
            output_string+= "{ "+ current.value + " } -> "
            current = current.next
        return output_string + "NULL"


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



