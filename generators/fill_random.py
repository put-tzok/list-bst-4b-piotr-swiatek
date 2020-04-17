from random import randint


def fill_random(size):
    array = []
    max_element_size = size * 100
    for i in range(size):
        array.append(randint(0, max_element_size))

    return array


