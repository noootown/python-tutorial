def calDelta(a1, b1, c1, a2, b2, c2, a3, b3, c3):
  return a1 * b2 * c3 + b1 * c2 * a3 + c1 * a2 * b3 -\
          a1 * c2 * b3 - b1 * a2 * c3 - c1 * b2 * a3
    

param = [float(i) for i in input("Input number a1 b1 c1 d1 a2 b2 c2 d2 a3 b3 c3 d3: ").split(' ')]

a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3 = param

delta = calDelta(a1, b1, c1, a2, b2, c2, a3, b3, c3)
deltax = calDelta(d1, b1, c1, d2, b2, c2, d3, b3, c3)
deltay = calDelta(a1, d1, c1, a2, d2, c2, a3, d3, c3)
deltaz = calDelta(a1, b1, d1, a2, b2, d2, a3, b3, d3)

print('Solve: ')
print('%.2fx + %.2fy + %.2fz = %.2f' % (a1, b1, c1, d1))
print('%.2fx + %.2fy + %.2fz = %.2f' % (a2, b2, c2, d2))
print('%.2fx + %.2fy + %.2fz = %.2f' % (a3, b3, c3, d3))
print('x = %.2f' % (deltax / delta))
print('y = %.2f' % (deltay / delta))
print('z = %.2f' % (deltaz / delta))

