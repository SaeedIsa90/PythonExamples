import tracemalloc


def calculate_triangle_area(h, b):
    a = (h * b)/2
    return a


def calculate_max(h, b):
    if h > b:
        return h
    else:
        return b


def allocate(i):
    return [10] * i


if __name__ == "__main__":
    tracemalloc.start()

    for (h, b) in zip(range(1, 15_000_000), range(15_000_000, 30_000_000)):
        area = calculate_triangle_area(h, b)

    for (h, b) in zip(range(1, 10_000_00), range(10_000_00, 20_000_00)):
        calculate_max(h, b)
    l = allocate(10000)
    snapshot = tracemalloc.take_snapshot()
    for stats in snapshot.statistics('lineno'):
        print(stats)
    print('done')
