from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:

    """
    Put docstring here
    """

    def __init__(self):
        self.rear = None
        self.front = None
        self.count = 0

    def enqueue(self, value):
        self.count += 1
        if self.front is None:
            self.front = Node(value)
            self.rear = self.front
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        self.count -= 1
        temporary_value = self.front
        self.front = self.front.next
        temporary_value.next = None
        return temporary_value.value

    def peek(self):
        if not self.front:
            raise InvalidOperationError
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        return False

