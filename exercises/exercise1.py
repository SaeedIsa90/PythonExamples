

def calculate_triangle_area(h, b):
    a = (h * b)/2
    print('Area is:', a)


if __name__ == "__main__":
    h = int(input('Enter H: '))
    b = int(input('Enter B: '))
    calculate_triangle_area(h, b)

