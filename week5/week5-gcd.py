while 1:
    a = int(input('a? '))
    b = int(input('b? '))

    while a != 0 and b != 0:
        if a >= b:
            a = a % b 
        else:
            b = b % a
    
    print('gcd: %d' % (b if a == 0 else a))

