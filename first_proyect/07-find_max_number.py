def find_max_number(numbers):
    if numbers:
        max_number = max(numbers)
        return max_number
    else:
        return None

lists_numbers = [4,5,6,7,12,2,3]
print(find_max_number(lists_numbers))