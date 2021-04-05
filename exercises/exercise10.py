def binary_search(lst, n):
    left = 0
    right = len(lst) - 1
    while left <= right:
        middle = (left + right)//2
        if n < lst[middle]:
            right = middle - 1
        elif n > lst[middle]:
            left = middle + 1
        else:
            return middle
    return -1


if __name__ == "__main__":
    lst = [1, 3, 4, 6, 9, 12, 15, 19, 25, 60, 120]
    idx = binary_search(lst, 25)
    print('Index is: ', idx)
