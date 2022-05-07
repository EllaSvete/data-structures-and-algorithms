
from multiprocessing.sharedctypes import Value


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


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

