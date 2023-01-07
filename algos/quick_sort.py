def partition(num_list, start, end):
    # choose pivot
    pivot = num_list[end]

    greater_element_iterator = start
    for i in range(start, end):
        if num_list[i] < pivot:
            # Swapping
            num_list[i], num_list[greater_element_iterator] = num_list[greater_element_iterator], num_list[i]
            greater_element_iterator += 1

    # Swapping pivot
    num_list[end], num_list[greater_element_iterator] = num_list[greater_element_iterator], num_list[end]
    return greater_element_iterator


def quick_sort(num_list, start, end):
    if start < end:
        pivot_idx = partition(num_list, start, end)

        # quick sort left part
        quick_sort(num_list, start, pivot_idx - 1)

        # quick sort right part
        quick_sort(num_list, pivot_idx + 1, end)


my_list = [20, 7, 1, 62, 33, 29, 12, 50]
quick_sort(my_list, 0, len(my_list)-1)
print(my_list)
