def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)

while 1:
    a = int(input('a? '))
    b = int(input('b? '))
    print(gcd(a, b))

