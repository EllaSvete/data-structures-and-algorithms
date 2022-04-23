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

class Node:
        # initializing Node class with parameters of self, vale, and next as a variable set to None
    def __init__(self, value, next=None):
        # here we set self.value to value, meaning the value of the node
        # and self.next to next which is is how we view the value of the next node
        self.value = value
        self.next = next


class TargetError:
    pass
