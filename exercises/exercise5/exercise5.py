def concatenate_names(file1, file2):
    fd1 = open(file1, 'r')
    fd2 = open(file2, 'r')

    res = open('res_names.txt', 'w')

    while True:
        l1 = fd1.readline()
        while l1 == '\n' or l1.isspace():
            l1 = fd1.readline()

        l2 = fd2.readline()
        while l2 == '\n' or l2.isspace():
            l2 = fd2.readline()

        if l1 != '':
            res.write(' '.join(l1.split()) + '\n')

        if l2 != '':
            res.write(' '.join(l2.split()) + '\n')

        if l1 == '' and l2 == '':
            break

    fd1.close()
    fd2.close()
    res.close()


if __name__ == '__main__':
    concatenate_names('names1.txt', 'names2.txt')
