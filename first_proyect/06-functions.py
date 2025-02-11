def squared(x: int):
    if type(x) != int:
        return "The number it has to be a int"
    else:
     y = x ** 2
     return y


assert  squared(2) == 4, "There is a mistake where"