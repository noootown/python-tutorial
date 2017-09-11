def toBinary(number, length):
    binary = [0] * length
    ptr = 0
    while number != 0:
        if number % 2 == 1:
            binary[ptr] = 1
        number //= 2
        ptr += 1
    return binary

while 1:
    num = int(input('How many number? '))

    for i in range(2 ** num):
        binary = toBinary(i, num)
        for j in range(num):
            if binary[j] == 1:
                print(j+1, end="")
                print(" ", end="")
        print("")
