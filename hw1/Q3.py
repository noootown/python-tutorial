def fac(n):
  s = 1
  for i in range(1, n + 1):
    s *= i
  return s

def c(n, m):
  return fac(n) / fac(m) / fac(n - m)

term = int(input("(1+x)^n, please input n: "))

print("(1+x)^%d = " % term)
print(" + ".join(["%dx^%d" % (c(term, t), t) for t in range(term + 1)]))

