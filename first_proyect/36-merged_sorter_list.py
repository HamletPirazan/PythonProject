def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    sorted_list = sorted(list1)
    return sorted_list

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))
print(merge_sorted_lists([1, 4, 6], [2, 3, 5]))
print(merge_sorted_lists([], [1, 2, 3]))
print(merge_sorted_lists([1, 2, 3], []))
print(merge_sorted_lists([], []))
