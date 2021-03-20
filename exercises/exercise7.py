def dividable_by_3(n):
    lst = []
    for i in range(1, n+1):
        if i %3 !=0:
            lst.append(i)

    print('List is: ', lst)
    print('Length is: ', len(lst))
    print('Sum is: ', sum(lst))


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    dividable_by_3(n)
