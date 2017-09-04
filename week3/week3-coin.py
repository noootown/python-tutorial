MONEY = [1000, 500, 100, 50, 10, 5, 1]
while 1:
    bill = [0] * len(MONEY)

    money = int(input('Change how much money? '))

    for i in range(len(MONEY)):
        bill[i] += money // MONEY[i]
        money %= MONEY[i]

    print(MONEY)
    print(bill)
