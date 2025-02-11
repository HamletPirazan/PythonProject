def calculate_average(numbers):
    length_numbers = len(numbers)
    if length_numbers != 0:

        total = 0
        for i in numbers:
            total = total + i

        return total / length_numbers
    else:
        return 0

print(calculate_average([5, 10, 15, 20]))
print(calculate_average([]))