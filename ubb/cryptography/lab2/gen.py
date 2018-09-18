from random import randint

T = 15
D = [5, 7, 10, 15, 20, 25, 50, 100, 200, 500, 1000, 2000, 3000, 4000, 5000]

for (index, value) in enumerate(D):
  print("generate " + str(value))
  with open(str(index) + ".in", "w") as f:
    x = randint(10 ** (value - 1), 10 ** value - 1)
    y = randint(10 ** (value - 1), 10 ** value - 1)
    f.write(str(value) + "\n" + str(x) + " " + str(y))
