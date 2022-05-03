from data_structures.stack import Stack


class PseudoQueue():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, value):
        # while not self.out_stack.is_empty():
        #     self.in_stack.push(self.out_stack.pop())
        self.in_stack.push(value)


    def dequeue(self):
        if self.out_stack.is_empty():
         while not self.in_stack.is_empty():
            item = self.in_stack.pop()
            self.out_stack.push(item)
        return self.out_stack.pop()

