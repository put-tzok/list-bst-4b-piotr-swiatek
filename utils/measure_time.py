import time
ONE_SECOND = 1000

REPEATS = 10


def measure_time(array, structure):
    start_time_append = time.time()
    for _ in range(REPEATS):
        for i in array:
            structure.append(i)
    end_time_append = time.time()
    time_append = round((end_time_append - start_time_append) * ONE_SECOND / REPEATS, 3)
    start_time_find = time.time()
    for _ in range(REPEATS):
        for i in array:
            structure.find(i)
    end_time_find = time.time()
    time_find = round((end_time_find - start_time_find) * ONE_SECOND / REPEATS, 3)
    return {
        'append': time_append,
        'find': time_find
    }

