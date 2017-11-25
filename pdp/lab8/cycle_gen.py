#!/usr/bin/python

import sys, getopt
from random import randint, shuffle

NS = {
  "small": [2, 10],
  "medium": [10, 12],
  "large": [12, 15],
}

def generate(now, inputFile, options):
  N = NS[now]
  n = randint(N[0], N[1])
  m = randint(n, n * (n - 1))
 # m = n * (n - 1)
  f = open(inputFile, "w")
  p = range(1, n + 1)
  shuffle(p)
  e = zip(p, p[1:] + p[:1])
  print(e)
  if options == "cycle":
    for i in range(m - n):
      x = randint(1, n)
      y = randint(1, n)
      while x == y or (x, y) in e:
        x = randint(1, n)
        y = randint(1, n)
      e.append((x, y))
  else:
    e = e[:-1]
    m = len(e)
  f.write(str(n) + " " + str(m) + "\n")
  shuffle(e)
  for edg in e:
    f.write(str(edg[0]) + " " + str(edg[1]) + "\n")
  f.close()

def main(argv):
  size = "small"
  inputFile = "0.in"
  options = "cycle"
  try:
    opts, args = getopt.getopt(argv,"h:s:i:o:",["size=", "input=", "option="])
  except getopt.GetoptError:
    print 'test.py -s <small | medium | large> -i <input> -o <no-cycle>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'test.py -s <small | medium | large>'
      sys.exit()
    elif opt in ["-s", "--size"]:
      size = arg
    elif opt in ["-i", "--input"]:
      inputFile = arg
    elif opt in ["-o", "--option"]:
      options = "no-cycle"
  print("Generating " + size + " test input = " + inputFile + " options = " + options)
  generate(size, inputFile, options)

if __name__ == "__main__":
   main(sys.argv[1:])
