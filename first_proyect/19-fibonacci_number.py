def find_fibonacci(n):
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a,b = 0,1

    for i in range(2, n+1):
        next_fibo = a + b
        a,b = b, next_fibo
    return b

print(find_fibonacci(10))