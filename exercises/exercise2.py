import math


def my_pow(x, y=7):
    res = 1
    for i in range(y):
        res *= x
    return res


def my_recursive_pow(x, y=7):
    if y == 0:
        return 1
    return x * my_recursive_pow(x, y-1)


def check_if_even_or_odd():
    while True:
        inp = input("Enter a number: ")

        if inp == "exit":
            print("End of program, thank you!!!")
            break

        if inp.isnumeric():
            int_inp = int(inp)
            if (int_inp % 2) == 0:
                # Even number
                print("Pow7 is: ", my_recursive_pow(int_inp))
            else:
                # Odd number
                print("Sqrt is: ", math.sqrt(int_inp))


if __name__ == "__main__":
    check_if_even_or_odd()
