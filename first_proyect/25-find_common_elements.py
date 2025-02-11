def find_common_elements(list1, list2):
    common_numbers = []
    for i in list1:
        for j in list2:
            if i == j:
                common_numbers.append(j)

    return common_numbers

print(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
