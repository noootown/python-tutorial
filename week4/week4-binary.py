while 1:
    a = int(input('number'))
    binary = []
    
    while 1:
        binary.append(a % 2)
        a = a // 2    
        if a == 0:
            break
    binary = binary[::-1]
    for i in range(len(binary)):
        print(binary[i],end = '')
    print('')
    
        
