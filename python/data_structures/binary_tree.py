
from multiprocessing.sharedctypes import Value
from data_structures.queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None, values=None):
        self.root = root
        if values:
            for value in values:
                self.add(value)


    def add(self, value):

        node = Node(value)

        if not self.root:
            self.root = node
            return

        current_node = self.root

        while current_node:
            if current_node.value > value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = node

                    return
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = node

                    return

        # breadth.enqueue(self.root)

        # while not breadth.is_empty():
        #     front = breadth.dequeue()
        #     if not front.left:
        #         front.left = node
        #         return
        # else:
        #     breadth.enqueue(front.left)

        # if not front.right:
        #     front.right = node
        #     return
        # else:
        #     breadth.enqueue(front.right)


    def pre_order(self):
        """
        traverse tree in pre-order fashion
        return list of the values in correct order
        """
        def walk(root, values):
        # task 1: do something

            if not root:
                return

            values.append(root.value)
        # task 2: go left
            walk(root.left, values)

        # task 3: go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def in_order(self):
        """
        traverse tree in pre-order fashion
        return list of the values in correct order
        """
        def walk(root, values):
        # task 1: do something

            if not root:
                return

        # task 2: go left
            walk(root.left, values)

            values.append(root.value)
        # task 3: go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values


    def post_order(self):
        """
        traverse tree in pre-order fashion
        return list of the values in correct order
        """
        def walk(root, values):
        # task 1: do something

            if not root:
                return

        # task 2: go left
            walk(root.left, values)

        # task 3: go right
            walk(root.right, values)

            values.append(root.value)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def find_maximum_value(self):
        # seeing the root is None to move towards traversal
        if self.root is None:
            return None
        # defining the traversal method to take in the root and the value
        def walk(root, max_val):
        # if the root is None return max_val which is set to 0
            if root is None:
                return max_val
        # if root value is greater than the max value then the new max value is equal to the root value
            if root.value > max_val:
                max_val = root.value
        # traverse the tree using recursion passing in left, right, and the new max. this is what is checking all the nodes
            max_val = walk(root.left, max_val)
            max_val = walk(root.right, max_val)

            return max_val

        # setting the result to the traversal where max starts at zero
        res = walk(self.root, 0)
        return res





