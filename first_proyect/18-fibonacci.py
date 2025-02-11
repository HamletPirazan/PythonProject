def fibonacci(n):
    fib_series = []


    if n <= 0:
        return fib_series
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]


    fib_series = [0, 1]


    for i in range(2, n):
        next_number = fib_series[i - 1] + fib_series[i - 2]
        if next_number > n:
            break
        fib_series.append(next_number)

    return fib_series



print(fibonacci(10))