from random import randint

#T = [3, 5, 10, 25, 50, 75, 100]
T = [100, 250, 500, 750, 1000, 1500, 2000]

def test(tid, n):
  with open("mult%d.in" % tid, "w") as f:
    print("generating %d" % tid)
    f.write(str(n) + "\n")
    for i in range(n):
      for j in range(n):
        f.write(str(randint(1, 100)) + " ")
      f.write("\n")
    for i in range(n):
      for j in range(n):
        f.write(str(randint(1, 100)) + " ")
      f.write("\n")
    for i in range(n):
      for j in range(n):
        f.write(str(randint(1, 100)) + " ")
      f.write("\n")

for (tid, n) in enumerate(T):
  test(tid, n)
