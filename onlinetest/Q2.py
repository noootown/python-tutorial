# 978-0-393-97950-3
isbn = input('Please input a ISBN: ')

isbn = ''.join(isbn.split('-'))

s = 0
for i in range(12):
    s += (3 if i % 2 else 1) * int(isbn[i])
s = 10 - s % 10

print(s == int(isbn[-1]))

