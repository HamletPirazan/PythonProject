numbers = [1, 2, 3, 4, 12, 2, 3]

max_number = numbers[0]

for i in numbers:
    if i > max_number:
        max_number = i
print("El número máximo es:", max_number)

i = 1
while i <= 5:
    print('*' *i)
    i += 1
print("Done")