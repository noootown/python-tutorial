while 1:
    num = int(input('Please input a number '))
    binary = []
    while num != 0:
        binary.append(num%2)
        num //= 2
    print(''.join([str(b) for b in binary[::-1]]))

