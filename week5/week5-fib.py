while 1:
    n = int(input('Fib(n)? '))
    n0, n1 = 0, 1
    if n < 2:
        print(n)
        continue

    for i in range(2, n+1):
        now = n1 + n0
        n0 = n1
        n1 = now
    print(now)

