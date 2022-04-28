from email import header


class LinkedList:
    # initializes class
    """
    Put docstring here
    """

    def __init__(self):
        # initializes attributes of the class
        # setting the head to be empty
        self.head = None

    def __str__(self):
        # setting a variable to an empty string to populate string with values as they come in
        # While the current value is equal to the input the current value will move on to the next value, if not it will return the input + null
        input = ""
        current = self.head
        while current:
            input += f"{{ {str(current.value)} }} -> "
            current = current.next
        return input + "NULL"



    def insert(self, value):
        # creating a new node with correct value which is the head
        self.head = Node(value, self.head)
        # we are saving address of next thing in the linked list
        #

    def includes(self, value):
        # setting the current node to the head
        current = self.head
        # while current node value is strictly equal to the value of the node return true
        while current:
            if current.value == value:
                return True
        # if current node is equal to the next node return false
            current = current.next

        return False

    def append(self, new_value):
        """
        set your your new node as an attribute to the new value of the Node class.
        self.head is the current node we are on
        the value of the head will be set to the value of the new node
        while that value is none, the value will become the value of the next node which is now the value of the end node.
        """
        end_node = Node(new_value)
        if self.head is None:
            self.head = end_node
            return
        else:
            held_value = self.head
            while held_value.next is not None:
                held_value = held_value.next
            held_value.next = end_node

    def insert_before(self, value, new_value):
        """
        make a new node
        iterate through the list looking for the element previous to it
        we can re-assign next to
        """
        # find the node we want to insert before
        # save value from previous node and check next value if next node is not before value, reassign temp
        # repeat
        # if next value is not before then don't reassign temp
        new_node = Node(new_value)
        current = self.head
        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError
        if current.value is value:
            new_node.next = self.head
            self.head = new_node
        while current.next is not None:
            if current.next.value is value:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next

    def insert_after(self, value, new_value):
        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError
        new_node = Node(new_value)
        current = self.head
        while current:
            if current.value is value:
                new_node.next = current.next
                current.next = new_node
                break

    def length_of_linked_list(self):
        n = 0
        current = self.head

        while current:
            current = current.next
            n += 1
        return n

    def kth_from_end(self, k):
        if k >= 0:
            current = self.head
            length = self.length_of_linked_list()
            target = length - k

            if target < 1:
                raise TargetError
            for i in range(1, target):
                current = current.next
            return current.value
        else:
            raise TargetError


class Node:
        # initializing Node class with parameters of self, vale, and next as a variable set to None
    def __init__(self, value, next=None):
        # here we set self.value to value, meaning the value of the node
        # and self.next to next which is is how we view the value of the next node
        self.value = value
        self.next = next


class TargetError(Exception):
    pass
