from random import randint

with open("graph2.in", "w") as f:
  n = 10000
  m = 25000
  f.write(str(n) + "\n")
  for i in range(n):
    f.write(randint(1, 100))
  e = 50000
  f.write("\n" + str(m) + "\n")
  for i in range(e):
    x = randint(1, m)
    y = randint(1, m)
    while x == y:
      y = randint(1, m)
    f.write(str(x) + " " + str(y) + "\n")



