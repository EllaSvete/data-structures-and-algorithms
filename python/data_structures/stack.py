from data_structures.linked_list import LinkedList

class IsEmptyError(Exception):
    pass

class Stack:
    """
    Put docstring here
    """
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, element):
        self.head = self.Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IsEmptyError("this stack is empty and cannot pop")
        result = self.head.element
        self.head = self.head.next
        self.size -= 1
        return result

    def top(self):
        if self.is_empty():
            raise IsEmptyError("retreive elements")
        return self.head.element


