def mergesort(sort_list):
    if len(sort_list) == 1:
        return sort_list
    left_list = mergesort(sort_list[:len(sort_list)//2])
    right_list = mergesort(sort_list[len(sort_list)//2:])
    left_index = 0
    right_index = 0
    output_list = []
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            output_list.append(left_list[left_index])
            left_index += 1
        else:
            output_list.append(right_list[right_index])
            right_index += 1
    if left_index == len(left_list):
        for thing in right_list[right_index:]:
            output_list.append(thing)
    else:
        for thing in left_list[left_index:]:
            output_list.append(thing)
    return output_list


some_list = [8, 7, 6, 5, 9, 0, 0, 4, 2, 3, 10, 20]
print(mergesort(some_list))