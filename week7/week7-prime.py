import time

primeList = []

MAX = 9999

for i in range(2, MAX):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        primeList.append(i)

while 1:
    sTime = time.time()

    num = int(input('Input number? '))
    print(' '.join([str(p) for p in primeList if p < num]))

    eTime = time.time()
    print(eTime - sTime)
