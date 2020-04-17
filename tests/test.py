from binary_search_tree.BinarySearchTree import BinarySearchTree
from linked_list.LinkedList import LinkedList

from generators.fill_increasing import fill_increasing
from generators.fill_random import fill_random

from utils.measure_time import measure_time
REPEATS = 10000

instances = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


def handle_linked_increasing(size):
    linked_list = LinkedList()
    array = fill_increasing(size)
    times = measure_time(array, linked_list)
    print('LL, append, {} size, increasing, {} ms'.format(size, times['append']))
    print('LL, find, {} size, increasing, {} ms'.format(size, times['find']))


def handle_linked_random(size):
    linked_list = LinkedList()
    array = fill_random(size)
    times = measure_time(array, linked_list)
    print('LL, append, {} size, random, {} ms'.format(size, times['append']))
    print('LL, find, {} size, random, {} ms'.format(size, times['find']))


def handle_bst_increasing(size):
    bst = BinarySearchTree()
    array = fill_increasing(size)
    times = measure_time(array, bst)
    print('BST, append, {} size, increasing, {} ms'.format(size, times['append']))
    print('BST, find, {} size, increasing, {} ms'.format(size, times['find']))


def handle_bst_random(size):
    bst = BinarySearchTree()
    array = fill_random(size)
    times = measure_time(array, bst)
    print('BST, append, {} size, random, {} ms'.format(size, times['append']))
    print('BST, find, {} size, random, {} ms'.format(size, times['find']))


def start():
    for instance in instances:
        try:
            size = instance * REPEATS
            handle_linked_increasing(size)
            handle_linked_random(size)
            handle_bst_random(size)
            handle_bst_increasing(size)
        except RuntimeError as re:
            print('Error in {}'.format(re))
