def check_if_prime(item):
    for i in range(2, (item//2)+1):
        if (item%i) == 0:
            return False
    return True


if __name__ == '__main__':
    lst = [1, 4, 11, 13, 25, 217, 2, 3, 10, 5, 7, 11, 23, 29, 31, 43, 47, 100, 102, 1004]
    prime_lst = []

    for item in lst:
        if check_if_prime(item):
            prime_lst.append(item)

    print('Prime lst is:')
    print(prime_lst)
