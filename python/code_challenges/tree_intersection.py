from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_one, tree_two):
    has_same_numbers = set()
    # setting the set function to a variable

    ht = Hashtable()
    # setting hashtable to a variable

    tree_one_val = BinaryTree.pre_order(tree_one)
    tree_two_val = BinaryTree.pre_order(tree_two)
    # calling the pre order function on binary tree

    for value in tree_one_val:
        ht.set(str(value), value)
    # calling set on the hash table and turning the value into a string

    for value in tree_two_val:
        if ht.contains(str(value)):
    # if it contains the same value then add it to the set

            has_same_numbers.add(value)

    return has_same_numbers

    # return the set of numbers
