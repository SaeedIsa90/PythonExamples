from time import perf_counter


def calculate_triangle_area(h, b):
    a = (h * b)/2
    return a


if __name__ == "__main__":
    start = perf_counter()

    for (h, b) in zip(range(1, 10_000_000), range(101, 25_000_000)):
        area = calculate_triangle_area(h, b)

    end = perf_counter()
    print('total time = ', end-start)
