#!/usr/bin/python

import sys, getopt
from random import randint

TYPES = {
  "small": [10**0, 10**1],
  "medium": [10**1, 10**3],
  "large": [10**3, 10**7],
}

NS = {
  "small": [1, 100],
  "medium": [100, 1000],
  "large": [100000, 500000],
}

def generate(now, inputFile, outputFile):
  N = NS[now]
  n = randint(N[0], N[1])
  T = TYPES[now]
  f = open(inputFile, "w")
  g = open(outputFile, "w")
  f.write(str(n) + "\n")
  s = 0
  for i in range(n):
    t = randint(T[0], T[1])
    s += t
    f.write(str(t) + "\n")
    g.write(str(s) + "\n")
  f.close()
  g.close()

def main(argv):
  size = "small"
  inputFile = "0.in"
  outputFile = "0.ok"
  try:
    opts, args = getopt.getopt(argv,"h:s:i:o:",["size=", "input=", "output="])
  except getopt.GetoptError:
    print 'test.py -s <small | medium | large> -i <input> -o <output>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'test.py -s <small | medium | large>'
      sys.exit()
    elif opt in ["-s", "--size"]:
      size = arg
    elif opt in ["-i", "--input"]:
      inputFile = arg
    elif opt in ["-o", "--output"]:
      outputFile = arg
  print("Generating " + size + " test input = " + inputFile
      + " output = " + outputFile)
  generate(size, inputFile, outputFile)

if __name__ == "__main__":
   main(sys.argv[1:])
