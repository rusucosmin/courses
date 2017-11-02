from os import sys, path
from random import randint

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
      print("ERROR: Symbols file not found!")
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
      f.write(buff)

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

  # method decides if _token is a symbol or an identifier
  def addToken(self, _token):
    # if the token is in the symbols table, then it's a symbol
    if _token in self.symbolsTable:
      return self.addSymbol(_token)
    # else, it must be an identifier
    else:
      return self.addIdentifier(_token)

  # method prints the symbol to the program internal form file outpu
  def addSymbol(self, _symbol):
    # if the symbol is in the symbol table
    if _symbol in self.symbolsTable:
      # print it
      self.appendToOutput(str(self.symbolsTable[_symbol]) + " 0\n")
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
        self.symbolsTable["identifier"] + " " + str(self.identifiersTable[_id]) + "\n")
    return True

  # method adds a constant to the table and prints it to the output file
  def addConstant(self, _val):
    # assign a new, unsued integer id for the current identifier
    if _val not in self.constantsTable:
      self.constantsTable[_val] = self.randomNotIn(self.constantsTable.values())
    # print to the program internl form output file
    self.appendToOutput(
        self.symbolsTable["constant"] + " " + str(self.constantsTable[_val]) + "\n")
    return True

  # generator method returns all the characters line by line
  def getNextChar(self):
    try:
      # open the file for reading
      f = open(self.fileName, "r")
      # read all the lines
      lines = f.readlines()
      # iterate through lines
      for lineIndex, line in enumerate(lines):
        # iterate through columns
        for columnIndex, ch in enumerate(line):
          # yield the line, column index and the current character
          yield [lineIndex, columnIndex, ch]
    # if file was not found, print error and fail fast
    except IOError:
      print("ERROR: Source file not found!")
      sys.exit()

  # method tokenize the source file
  def tokenize(self):
    # get the generator
    charIterator = self.getNextChar()
    try:
      # get the next values from the generator
      (i, j, ch) = next(charIterator)
      # we iterate while we get a StopIteration exception
      while True:
        # in case we have an alphabet character (a, b, .. z, A, B, .. Z)
        if ch.isalpha():
          # variable to store the current identifier
          _id = ""
          # we iterate with the iterator while we have valid identifier characters
          while ch.isalpha() or ch == '_':
            # append the current character to _id
            _id += ch
            # get the next character
            (i, j, ch) = next(charIterator)
          # at the end, if the lenght of the iterator is more than the max allowed lenght
          # throw an error, and fail fast
          if len(_id) > 250:
            print("ERROR: Identifier has too many characters. (line, col) = (%d, %d)" % (i, j))
            sys.exit()
          # add the token to the interal hashmaps
          self.addToken(_id)
          _id = ""
        # in case we have a digit (0-9)
        elif ch.isdigit():
          # variable stores the current constant
          _val = ""
          # while there is a digit or if the current character is .
          while ch.isdigit() or ch == '.':
            # append the character to the constant
            _val += ch
            # get next character
            (i, j, ch) = next(charIterator)
          # add the constant to the program internal form and to the internal hashmaps
          self.addConstant(_val)
        # ignore whitespace characters
        elif ch.isspace():
          # get the next character
          (i, j, ch) = next(charIterator)
        # else, we may have a symbol or an invalid identifier
        else:
          # get the first character and store it in the _id variable
          _id = ch
          # try to get the second one for cases like >=, <=, == and !=
          try:
            # store last character
            last = ch
            # get the next cahracter
            (i, j, ch) = next(charIterator)
            # if we are in one of the cases >=, <=, == or !=, we update the variable
            if (last == '>' or last == '<' or last == '=' or last == '!') and ch == '=':
              _id = _id + ch
          except StopIteration:
            # no other character left to get, we simply pass cause we may have }
            pass
          # if we couldn't add the symobl, we throw an error because it is an unexpected
          # symbol identifier
          if not self.addSymbol(_id):
            print("ERROR: Syntax Error detected at (line, col) = (%d, %d)" % (i, j))
            print("ERROR: Unexpected token '%s'" % _id)
            sys.exit()
    # in case we reached the end of the iteration
    except StopIteration:
      self.writeTables()
      print("> finish")
      return

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
  print("> scanning " + str(sys.argv[1]) + "...")
  # scan that filename
  scan(sys.argv[1])
