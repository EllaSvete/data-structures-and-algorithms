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
            self.rear = Node(value)


    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        self.count -= 1
        node_to_remove = self.front
        if self.count == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        return node_to_remove.value


    def peek(self):
        if not self.front:
            raise InvalidOperationError
        else:
            return self.front.value



    def is_empty(self):
        if self.front is None:
            return True
        return False



# Enqueue O(1)
#
