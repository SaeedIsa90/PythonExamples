def selection_sort(lst):
    for i in range(len(lst)):
        # Find the max element in remaining lst
        max_idx = 0
        for j in range(0, len(lst)-i):
            if lst[max_idx] < lst[j]:
                max_idx = j

        last_idx = (len(lst)-i)-1
        # Swap elements - founded max with last
        lst[last_idx], lst[max_idx] = lst[max_idx], lst[last_idx]
    return lst


if __name__ == '__main__':
    lst = [3, 10, 4, 2, 9, 1]
    sorted_lst = selection_sort(lst)
    print(sorted_lst)
