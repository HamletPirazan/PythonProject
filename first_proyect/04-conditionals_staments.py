number = int(input("Write your number"))

error = "Your variable is not bigger than 1"

if number == 1:
    print("Your are bigger than '1'" + str(number))
elif number == 0:
    print("X is equal to 0")
elif 10 < number < 12:
    print("X esta entre 10 y 12")
else:
    print(error)
