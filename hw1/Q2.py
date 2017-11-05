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
  num = int(input('Input number? '))
  for p in primeList:
    if num % p == 0:
      print("%d = %d * %d" % (num, p, num / p))
      break
