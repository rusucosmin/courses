from random import randint

def testRandom(fileName, n, m):
    f = open(fileName, "w")
    f.write("%d %d\n" % (n, m))
    f.write(" ".join([str(i) for i in range(1, n + 1)]) + "\n")
    edges = {}
    for i in range(m):
        found = False
        while not found:
            x = randint(1, n)
            y = randint(1, n)
            while x == y:
                y = randint(1, n)
            if x > y:
                (x, y) = (y, x)
            if (x, y) in edges:
                continue
            else:
                found = True
                f.write("%d %d\n" % (x, y))
                edges[(x, y)] = True

    f.close()

#testRandom("input1.in", 5, 10)
#testRandom("input2.in", 10, 30)
#testRandom("input3.in", 15, 60)
testRandom("input4.in", 15, 15 * 7)
