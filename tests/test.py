from binary_search_tree.BinarySearchTree import BinarySearchTree
from linked_list.LinkedList import LinkedList

from generators.fill_increasing import fill_increasing
from generators.fill_random import fill_random

from utils.measure_time import measure_time

instances = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


def handle_linked_increasing(size):
    linked_list = LinkedList()
    array = fill_increasing(size)
    times = measure_time(array, linked_list)
    print('LL, append, {} size, increasing, {} s'.format(size, round(times['append'] / size, 5)))
    print('LL, find, {} size, increasing, {} s'.format(size, round(times['find'] / size, 5)))


def handle_linked_random(size):
    linked_list = LinkedList()
    array = fill_random(size)
    times = measure_time(array, linked_list)
    print('LL, append, {} size, random, {} s'.format(size, round(times['append'] / size, 5)))
    print('LL, find, {} size, random, {} s'.format(size, round(times['find'] / size, 5)))


def handle_bst_increasing(size):
    bst = BinarySearchTree()
    array = fill_increasing(size)
    times = measure_time(array, bst)
    print('BST, append, {} size, increasing, {} s'.format(size, round(times['append'] / size, 5)))
    print('BST, find, {} size, increasing, {} s'.format(size, round(times['find'] / size, 5)))


def handle_bst_random(size):
    bst = BinarySearchTree()
    array = fill_random(size)
    times = measure_time(array, bst)
    print('BST, append, {} size, random, {} s'.format(size, round(times['append'] / size, 5)))
    print('BST, find, {} size, random, {} s'.format(size, round(times['find'] / size, 5)))


def start():
    for instance in instances:
        try:
            handle_linked_increasing(instance)
            handle_linked_random(instance)
            handle_bst_increasing(instance)
            handle_bst_random(instance)
        except RuntimeError as re:
            print('Error in {}'.format(re))
