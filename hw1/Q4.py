with open('99.txt', 'w') as file:
  for i in range(1, 10):
    for j in range(1, 10):
      file.write('%d*%d=%d\t' % (i, j, i * j))
    file.write('\n')
