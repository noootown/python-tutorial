primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

num = int(input('Please input a number: '))

l = []

while num != 1:
    for p in primeList:
        if num % p == 0:
            l.append(p)
            num /= p
            break

print(' * '.join([str(ll) for ll in l]))

