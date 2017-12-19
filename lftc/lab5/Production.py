"""
January 27, 2016
"""

from Symbol import Symbol

class Production(object):
  """Production"""
  index = 1

  def __init__(self, non_terminal, production, grammar, dot = 0):
    super(Production, self).__init__()
    # If the production string is 
    #   A := a b . C
    # non_terminal = A
    # production = [a, b, C]
    # dot = 2 (position of dot)

    self.non_terminal = non_terminal
    self.production = production
    self.dot = dot
    self.grammar = grammar
    self.index = Production.index
    Production.index += 1

  def next_symbol(self):
    # Returns next symbol after dot.
    if self.dot < len(self.production): return self.production[self.dot] 

  def increment_dot(self):
    # Increments the position of dot.
    self.dot += 1

  def __eq__(self, other):
    # Two productions are equal when they have same non terminal, productions 
    # and dot.
    return True if self.non_terminal == other.non_terminal and \
           self.production == other.production and \
           self.dot == other.dot else False

  def __str__(self):
    r = ""
    found = False
    for i, s in enumerate(self.production):
      if i == self.dot:
        r += ". "
        found = True
      r += "%s " %(s.symbol)
    if not found:
      r += "."

    return self.non_terminal + " := " + r

  def is_next_terminal(self):
    # Returns True if next symbol is a terminal, otherwise False is returned.
    return self.next_symbol().is_terminal() if self.next_symbol() else None


class ProductionGenerator(object):
  """ProductionGenerator. Generates productions of a grammar"""
  def __init__(self, str_productions, grammar):
    self.str_productions = str_productions
    self.grammar = grammar

  def generate(self):
    # Generates productions of the grammar.

    # super(ProductionGenerator, self).__init__()
    left, right = self.str_productions.split(":=")
    left = left.strip()
    productions_split = right.split("|")
    productions = []
    for str_production in productions_split:
      q = []
      for symbol in str_production.strip().split(" "):
        if symbol != "E": # TODO: Set Epsila as global variable.
          q.append(Symbol(symbol, self.grammar))
      productions.append(q)

    # Create a list of production objects and return
    return [Production(left, production, self.grammar) \
           for production in productions]
    

def main():
  # # ps = Production.get("B := a b c | d e f | x B")
  # # ps = Production.get("B := a b c | d e f | x B")
  ps = ProductionGenerator("B := a b c | X e f | E", None)
  generated_produtions = ps.generate()

  # print ps
  # # ps = Production.get("S' := S")
  for p in generated_produtions:
    print p


  # a = Production()

if __name__ == '__main__':
  main()
