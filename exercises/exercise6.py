def get_list():
    inp = input("Enter a list: ")
    lst = []
    for i in inp.split():
        lst.append(int(i))
    return lst


def check_ascending(left):
    for i in range(len(left)-1):
        if left[i] >= left[i+1]:
            return False
    return True


def check_descending(right):
    for i in range(len(right)-1):
        if right[i] <= right[i+1]:
            return False
    return True


def check_if_middle_peak(lst):
    m = len(lst)//2
    if check_ascending(lst[:m+1]):
        if check_descending(lst[m:]):
            return True
    return False


if __name__ == '__main__':
    num_lst = get_list()
    res = check_if_middle_peak(num_lst)
    if res:
        print('Yes middle peak!! :) ')
    else:
        print('Not middle peak!! :( ')
