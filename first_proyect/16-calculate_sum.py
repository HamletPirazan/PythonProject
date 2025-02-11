def sum_of_digits(num: int):
    total = 0
    divide_number = str(num)
    for i in divide_number:
        total += int(i)
    return total

print(sum_of_digits(0))