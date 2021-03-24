def ascii_func(sentence):
    odd = ''
    even = ''
    div_by3 = ''

    for i in sentence:
        ascii_value = ord(i)
        if (ascii_value % 2) == 1:
            odd += i
        else:
            even += i
        if (ascii_value % 3) == 0:
            div_by3 += i

    print('Odd: ', odd)
    print('Even: ', even)
    print('Div By3: ', div_by3)


if __name__ == '__main__':
    inp = input('Enter a sentence: ')
    ascii_func(inp)
