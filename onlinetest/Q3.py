num = [int(i) for i in input('Please enter a five digit number: ')]
sum = 0
for i in num:
    sum += (not i % 2) * i

print('sum %d' % sum)

