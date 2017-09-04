def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

while 1:
    n = int(input('Fib(n)? '))
    print(fib(n))

