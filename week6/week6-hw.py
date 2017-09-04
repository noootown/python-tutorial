def printList(num):
    l, digit = [], 1
    while num != 0:
        if num % 2 == 1:
            l.append(str(digit))
        digit += 1
        num //= 2
    print(' '.join(l))

while 1:
    n = int(input('How many number? '))
    for i in range(2 ** n):
        printList(i)

