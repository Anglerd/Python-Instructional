this_list = [5, 8, 6, 4, 3, 7, 8, 9]


def merge_sort(some_list):
    if some_list.__len__() > 1:
        midpoint = int(round(some_list.__len__() / 2, 0))
        list1 = merge_sort(some_list[midpoint:])
        list2 = merge_sort(some_list[:midpoint])
    else:
        return some_list
    index1 = index2 = 0
    merge = []
    while index1 < list1.__len__() and index2 < list2.__len__():
        if list1[index1] < list2[index2]:
            merge.append(list1[index1])
            index1 += 1
        else:
            merge.append(list2[index2])
            index2 += 1
    if index1 < list1.__len__():
        for num in list1[index1:]:
            merge.append(num)
    else:
        for num in list2[index2:]:
            merge.append(num)
    return merge


print(merge_sort(this_list))
