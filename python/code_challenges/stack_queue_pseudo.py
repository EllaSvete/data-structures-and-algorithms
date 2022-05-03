from data_structures.linked_list import Node
from data_structures.stack import Stack


class PseudoQueue():
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, value):
        self.inbox.push(value)


    def dequeue(self):
        return self.inbox.pop()
        # if self.inbox.is_empty:
        #     while self.inbox.size() > 0:
        #         self.outbox.push(self.inbox.pop())
        # return self.outbox.items.pop()

