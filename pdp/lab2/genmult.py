def test(t, n):
  print("test " + str(t))
  with open("mult" + str(t) + ".in", "w") as f:
    f.write(str(n) + " " + str(n) + " " + str(n) + "\n")
    for i in range(n):
      for j in range(n):
        f.write(str(i + j) + " ")
      f.write("\n")
    for i in range(n):
      for j in range(n):
        f.write("1 " if i == j else "0 ")
      f.write("\n")

test(1, 100)
test(2, 200)
test(3, 500)
test(4, 1000)
test(5, 2000)
