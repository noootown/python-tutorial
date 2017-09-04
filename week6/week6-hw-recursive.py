def printAll(depth, l):
    if depth == 0:
        print(' '.join(l))
        return

    printAll(depth - 1, [] + l)
    printAll(depth - 1, [str(depth)] + l)

while 1:
    printAll(int(input('How many number? ')), [])

