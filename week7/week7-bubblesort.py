while 1:
    l = [int(ll) for ll in input('Please sort list: ').split(' ')]

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] > l[i]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    
    l = [str(ll) for ll in l]
    
    print(' '.join(l))
    print(' '.join(l[::-1]))

