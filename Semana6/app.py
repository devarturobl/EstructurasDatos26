def fibonacci(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

print([fibonacci(i) for i in range(10)])





