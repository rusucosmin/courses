from os import sys

class Scanner:
  def __init__(self, filename):
    self.filename = filename
    # TODO: handle file not found exception
    self.f = open(filename, "r")

  # generator for each character in the source file
  def nextChar(self):
    for line in self.f.readlines():
      for ch in line:
        yield ch

def scan(filename):
  s = Scanner(filename)
  _char = s.nextChar()
  for ch in s.nextChar():
    print(ch)

if __name__ == '__main__':
  print("scanning " + str(sys.argv[1]))
  scan(sys.argv[1])
