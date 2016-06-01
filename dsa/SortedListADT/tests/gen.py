from random import randint

T = [10, 100, 1000, 2500, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 250000, 300000, 400000, 500000, 500000, 500000, 500000, 500000, 500000]
v = [2 ** (i + 11) for i in range(20)]

print(v)
for i in range(len(T)):
    print("> Generating test" + str(i) + ".in <")
    f = open("test" + str(i) + ".in", "w");
    n = T[i]
    f.write(str(n) + "\n")
    for j in range(n):
        x = randint(0, v[i])
        y = randint(0, v[i])
        if x > y:
            (x, y) = (y, x)
        f.write(str(x) + " " + str(y) + "\n")
    f.close()
