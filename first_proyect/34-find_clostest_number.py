def find_closest_number(numbers, target):
    closest_number = None
    min_difference = float('inf')
    for i in numbers:
        difference = abs(i - target)

        if difference < min_difference:
            min_difference = difference
            closest_number = i
    return closest_number
print(find_closest_number([2, 4, 8, 10], 6))