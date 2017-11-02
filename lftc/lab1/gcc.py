from os import sys
from random import randint

class Scanner:
  def __init__(self, fileName, outputFileName = "output.txt"):
    self.fileName = fileName
    self.outputFileName = outputFileName
    open(self.outputFileName, 'w').close()
    self.outputIdentifiersTable = "output_identifiers_table.txt"
    self.outputConstantsTable = "output_constants_table.txt"
    self.symbolsTable = {}
    self.identifiersTable = {}
    self.constantsTable = {}
    self.populateSymbolsTable()

  def populateSymbolsTable(self):
    try:
      f = open("symbols.txt")
      for line in f.readlines():
        (symbol, sid) = line.split()
        self.symbolsTable[symbol] = sid
    except IOError:
      print("ERROR: Symbols file not found!")
      sys.exit()

  def randomNotIn(self, values):
    r = randint(1, 100000)
    while r in values:
      r = randint(1, 100000)
    return r

  def appendToOutput(self, buff):
    with open(self.outputFileName, "a") as f:
      f.write(buff)

  def writeTables(self):
    with open(self.outputIdentifiersTable, "w") as f:
      for (key, val) in self.identifiersTable.iteritems():
        f.write("%s %s\n" % (key, val))
    with open(self.outputConstantsTable, "w") as f:
      for (key, val) in self.constantsTable.iteritems():
        f.write("%s %s\n" % (key, val))

  def addToken(self, _token):
    if _token in self.symbolsTable:
      return self.addSymbol(_token)
    else:
      return self.addIdentifier(_token)

  def addSymbol(self, _symbol):
    if _symbol in self.symbolsTable:
      self.appendToOutput(str(self.symbolsTable[_symbol]) + "\n")
      return True
    else:
      return False

  def addIdentifier(self, _id):
    self.identifiersTable[_id] = self.randomNotIn(self.identifiersTable.values())
    self.appendToOutput(
        self.symbolsTable["identifier"] + " " + str(self.identifiersTable[_id]) + "\n")
    return True

  def addConstant(self, _val):
    self.constantsTable[_val] = self.randomNotIn(self.constantsTable.values())
    self.appendToOutput(
        self.symbolsTable["constant"] + " " + str(self.constantsTable[_val]) + "\n")
    return True

  def getNextChar(self):
    try:
      f = open(self.fileName, "r")
      lines = f.readlines()
      for lineIndex, line in enumerate(lines):
        for columnIndex, ch in enumerate(line):
          yield [lineIndex, columnIndex, ch]
    except IOError:
      print("ERROR: Source file not found!")
      sys.exit()

  def tokenize(self):
    charIterator = self.getNextChar()
    try:
      (i, j, ch) = next(charIterator)
      while True:
        if ch.isalpha():
          _id = ""
          while ch.isalpha() or ch == '_':
            _id += ch
            (i, j, ch) = next(charIterator)
          self.addToken(_id)
        elif ch.isdigit():
          _val = ""
          while ch.isdigit() or ch == '.':
            _val += ch
            (i, j, ch) = next(charIterator)
          self.addConstant(_val)
        elif ch.isspace():
          (i, j, ch) = next(charIterator)
        else:
          _id = ch
          try:
            last = ch
            (i, j, ch) = next(charIterator)
            if (last == '>' or last == '<' or last == '=' or last == '!') and ch == '=':
              _id = _id + ch
          except StopIteration:
            pass
          if not self.addSymbol(_id):
            print("ERROR: Syntax Error detected at (line, col) = (%d, %d)" % (i, j))
            print("ERROR: Unexpected token '%s'" % _id)
            sys.exit()
    except StopIteration:
      self.writeTables()
      print("> finish")
      return

def scan(filename):
  s = Scanner(filename)
  s.tokenize()

if __name__ == '__main__':
  print("> scanning " + str(sys.argv[1]) + "...")
  scan(sys.argv[1])
