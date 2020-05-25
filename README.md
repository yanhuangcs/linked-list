# Singly Linked List

## A folder named linked_list which contains a file called linked_list.py

### Fatures in linked_list.py
A Node class that has properties for the value stored in the Node, and a pointer to the next Node.

A LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

### Methods in LinkedList class:
A method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.

A method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

A method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## A folder named tests with test_linked_list.py testing the functions in linked_list.py
### Tests cover:
Can successfully instantiate an empty linked list
Can properly insert into the linked list
The head property will properly point to the first node in the linked list
Can properly insert multiple nodes into the linked list
Will return true when finding a value within the linked list that exists
iWill return false when searching for a value in the linked list that does not exist

# Doubly Linked List
Same methods as singly linked list
