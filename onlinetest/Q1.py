arr = [int(i) for i in input('Please enter: ').split(' ')]
for i in range(4):
    for j in range(4):
        print('%d\t' % arr[4*i+j], end='')
    print('\n')

print('sum of row: %d %d %d %d' % (sum(arr[0:4]), sum(arr[4:8]),sum(arr[8:12]),sum(arr[12:16]),))

c1 = arr[0] + arr[4] + arr[8] + arr[12]
c2 = arr[1] + arr[5] + arr[9] + arr[13]
c3 = arr[2] + arr[6] + arr[10] + arr[14]
c4 = arr[3] + arr[7] + arr[11] + arr[15]

print('sum of column: %d %d %d %d' % (c1, c2, c3, c4))

d1 = arr[0] + arr[5] + arr[10] + arr[15]
d2 = arr[3] + arr[6] + arr[9] + arr[12]
print('sum of diagonal: %d %d' % (d1, d2))
