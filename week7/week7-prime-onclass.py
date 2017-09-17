import time

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

while 1:
    num = int(input("Input number? "))
    primeList = []
    sTime = time.time()
    for i in range(2, num):
        if isPrime(i):
            primeList.append(i)
    eTime = time.time()
    print(eTime - sTime)

    # print(' '.join([str(p) for p in primeList]))

