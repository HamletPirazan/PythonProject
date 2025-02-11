def remove_duplicates(input_list):
    unique_elements = set()
    result = []
    for item  in input_list:
        if item not in unique_elements:
            unique_elements.add(item)
            result.append(item)

    return result


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates(['apple', 'banana', 'apple', 'cherry']))
print(remove_duplicates([1, 2, 3]))
print(remove_duplicates([]))