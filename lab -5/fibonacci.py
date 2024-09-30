def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

N = 10
fib_numbers = fibonacci(N)
squared_fib_numbers = list(map(lambda x: x ** 2, fib_numbers))

print(squared_fib_numbers)
