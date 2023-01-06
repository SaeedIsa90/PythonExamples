def merge_sort(num_list):
    # Stop condition
    if len(num_list) <= 1:
        return

    # find the middle index
    mid = len(num_list) // 2  # integer
    left = num_list[:mid]  # left part [0->mid]
    right = num_list[mid:]  # right part

    # solve left part
    merge_sort(left)

    # solve right part
    merge_sort(right)

    l_idx = r_idx = k_idx = 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            num_list[k_idx] = left[l_idx]
            l_idx += 1
        else:
            num_list[k_idx] = right[r_idx]
            r_idx += 1
        k_idx += 1

    while l_idx < len(left):
        num_list[k_idx] = left[l_idx]
        l_idx += 1
        k_idx += 1

    while r_idx < len(right):
        num_list[k_idx] = right[r_idx]
        r_idx += 1
        k_idx += 1


# Examples:
my_list = [20, 7, 1, 62, 33, 29, 12, 50]
merge_sort(my_list)
print(my_list)
