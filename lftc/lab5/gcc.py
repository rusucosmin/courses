from os import sys, path
from random import randint
from finite_automata import FiniteAutomata
import json

# Class acts as a parser.
#     parametrs: fileName - the source of the toy language source code
class Scanner:
  # Consturctor for the Scanner, takes as a parameter the fileName consisting of the
  # source code that we want our lexer to tokenize
  def __init__(self, fileName):
    # filename refers to the toy language source code
    self.fileName = fileName
    # file to store the program internal form
    self.outputFileName = path.splitext(path.basename(fileName))[0] + "_pif.txt"
    # clear file if already exist
    open(self.outputFileName, 'w').close()
    # file to store the identifiers table
    self.outputIdentifiersTable = path.splitext(path.basename(fileName))[0] + "_id_table.txt"
    # file to store the constants table
    self.outputConstantsTable = path.splitext(path.basename(fileName))[0] + "_const_table.txt"
    # hashtable for all the program symbols (if, for, while, else, int, float, etc)
    self.symbolsTable = {}
    # hashtable for storing the identifiers, as a pair identifier -> integer id
    self.identifiersTable = {}
    # hashtable for storing the identifiers, as a pair constant -> integer id
    self.constantsTable = {}
    # load all the toy language symbols
    self.populateSymbolsTable()
    # Finite automatas
    with open('symbols.json') as f:
      self.symbols_fa = FiniteAutomata(json.load(f))
    with open('identifier.json') as f:
      self.identifers_fa = FiniteAutomata(json.load(f))
    with open('constant.json') as f:
      self.constants_fa = FiniteAutomata(json.load(f))

  # method loads symbol table in memory from the disc
  def populateSymbolsTable(self):
    try:
      # open the file
      f = open("symbols.dat")
      # iterate through its lines
      for line in f.readlines():
        # get the symbol and the symbol id
        (symbol, sid) = line.split()
        # add to the symbols table
        self.symbolsTable[symbol] = sid
    except IOError:
      # In case there is no such file, fail fast!
      print("> Error: Symbols file not found!")
      sys.exit()

  # method returns a random integer that is not in the values array
  def randomNotIn(self, values):
    # returns a random vaue between 1 and 100000
    r = randint(1, 100000)
    # while that value already exists in the array values
    while r in values:
      # generate a new one
      r = randint(1, 100000)
    # return the number generated
    return r

  # method append buff to the file outputFileName
  def appendToOutput(self, buff):
    # open file
    with open(self.outputFileName, "a") as f:
      # write the string buff as a new line
      f.write(buff + " ")

  # method write the identifier and constant tables
  def writeTables(self):
    # open file for identifiers table
    with open(self.outputIdentifiersTable, "w") as f:
      # iterate through the identifiers table
      for (key, val) in self.identifiersTable.iteritems():
        # write the pair on a new line
        f.write("%s %s\n" % (key, val))
    # open file for constant table
    with open(self.outputConstantsTable, "w") as f:
      # iterate through the constants table
      for (key, val) in self.constantsTable.iteritems():
        # write the pair on a new line
        f.write("%s %s\n" % (key, val))

  # method prints the symbol to the program internal form file output
  def addSymbol(self, _symbol):
    # if the symbol is in the symbol table
    if _symbol in self.symbolsTable:
      # print it
      self.appendToOutput(str(self.symbolsTable[_symbol]))
      return True
    else:
      # return false because _symbol is not a valid symbol, and then throw an error
      return False

  # method prints identifier and it's id to the output file
  def addIdentifier(self, _id):
    # assign a new, unused integer id for the current identifier
    if _id not in self.identifiersTable:
      self.identifiersTable[_id] = self.randomNotIn(self.identifiersTable.values())
    # print to program internal form output file
    self.appendToOutput(
        self.symbolsTable["identifier"])
    return True

  # method adds a constant to the table and prints it to the output file
  def addConstant(self, _val):
    # assign a new, unsued integer id for the current identifier
    if _val not in self.constantsTable:
      self.constantsTable[_val] = self.randomNotIn(self.constantsTable.values())
    # print to the program internl form output file
    self.appendToOutput(
        self.symbolsTable["constant"])
    return True

  # method tokenize the source file
  def tokenize(self):
    try:
      # read the file
      f = open(self.fileName, "r")
      # iterate on all the read lines
      for (i, line) in enumerate(f.readlines()):
        program = line
        while program != "":
          program = program.strip()
          # get the longest accepted prefix among all of the 3 finite automatas
          _sym = self.symbols_fa.longest_accepted_prefix(program)
          _id = self.identifers_fa.longest_accepted_prefix(program)
          _const = self.constants_fa.longest_accepted_prefix(program)
          # some of the symbols are also accepted identifiers (eg: while, int, etc)
          # in case they are eqla, symbols have higher priority
          if _sym == _id:
            _id = None
          if _id is not None and _id != "":
            if len(_id) > 250:
              print("> Error: Identifier has too many characters, line %d." % (i + 1))
              sys.exit(1)
            # add the token to the interal hashmaps
            self.addIdentifier(_id)
            program = program[len(_id):]
          elif _sym is not None and _sym != "":
            self.addSymbol(_sym)
            program = program[len(_sym):]
          elif _const is not None and _const != "":
            self.addConstant(_const)
            program = program[len(_const):]
          else:
            print("> Error: Syntax error. Unexpected token at line %d:%s" % (i + 1, program))
            sys.exit(1)
      self.writeTables()
    except IOError:
      print("> Error: Source file not found!")
      sys.exit(1)

# method scans and tokenize the filename source code
def scan(filename):
  # create the scaner
  s = Scanner(filename)
  # call the tokenize method
  s.tokenize()

# if name is main
if __name__ == '__main__':
  # get the first argument of the args
  # log it
  if len(sys.argv) > 1:
    print("> Scanning " + str(sys.argv[1]) + "...")
    # scan that filename
    scan(sys.argv[1])
  else:
    scan("main.cpp")
  print("> Done")

