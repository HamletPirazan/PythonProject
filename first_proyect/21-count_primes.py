def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    counter = 0
    for i in range(2, n):
        if is_prime(i):
            counter+=1
    return counter

print(count_primes(10))