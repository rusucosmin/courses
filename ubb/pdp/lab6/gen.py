from random import randint

T = [10, 50, 100, 500, 1000, 2000, 5000, 10000, 100000, 250000]

def test(tid, n):
  with open("tests/%d.in" % tid, "w") as f:
    f.write("%d\n" % n)
    for i in range(n):
      f.write("%d " % randint(1, 100))
    f.write("\n")
    for i in range(n):
      f.write("%d " % randint(1, 100))

for i, t in enumerate(T):
  print("%d %d" % (i, t))
  test(i, t)
