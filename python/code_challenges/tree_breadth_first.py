from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):

    queue_filled = []

    if tree is None:
        return queue_filled

    queue = Queue()

    if tree.root:
        queue.enqueue(tree.root)

    while queue.front:
        item = queue.dequeue()
        queue_filled.append(item.value)

        if item.left:
            queue.enqueue(item.left)

        if item.right:
            queue.enqueue(item.right)

    return queue_filled

