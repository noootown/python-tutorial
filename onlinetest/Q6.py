def getFactorial(n):
    s = 1
    for i in range(2, n + 1):
        s/= i
    return s

n = int(input('Please input a number: '))

sin1 = 0

for i in range(n):
    sin1 += (1 if (2 * i + 2) % 4 else -1) * getFactorial(2 * i + 1)
    print('Term %d, sin 1 = %f' % (i + 1, sin1))

