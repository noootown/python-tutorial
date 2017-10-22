num = int(input('Enter a number between 0 and 32767: '))
binary = [0] * 5
step = 0
while num != 0:
    binary[step] = num % 8
    num //= 8
    step += 1
print(''.join([str(b) for b in binary[::-1]]))

