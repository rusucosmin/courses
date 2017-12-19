"""
February 4, 2016

Generates First and Follow of a grammar.
"""

epsila = "E"
marker = "$"

class First_Follow(object):
  """Class to find first and follow of a grammar"""
  def __init__(self, grammar):
    super(First_Follow, self).__init__()
    self.grammar = grammar

    self.first = {}
    self.follow = {}

    for symbol in self.grammar.non_terminals:
      self.calculate_first(symbol)
      self.calculate_follow(symbol)

  def get_first(self, symbol):
    return self.first[symbol]

  def get_follow(self, symbol):
    return self.follow[symbol]

  def has_epsila_derivation(self, symbol):
    # Returns True if any production of the symbol has epsila.
    for production in self.grammar.get(symbol):
      if not len(production.production):
        return True

  def calculate_first(self, g_symbol):
    # Calculates First of the symbol. Returns a list of symbols and also 
    # places it in first dict.

    if g_symbol in self.grammar.terminals or g_symbol == epsila:
      return [g_symbol]

    first_set = set()
    
    # Get productions of given symbol only.
    productions = self.grammar.get(g_symbol)

    for production in productions:
      if len(production.production) == 0:
        first_set.add(epsila)
      for symbol in production.production:
        first_value = symbol.symbol
        if first_value in self.grammar.terminals:
          first_set.add(first_value)
          break
        elif first_value == epsila:
          first_set.add(epsila)
          break
        elif first_value in self.grammar.non_terminals:
          first_set.update(self.calculate_first(first_value))
          # Check whether it gives epsila derivation. In that case,
          # see the first of next literal.
          if not self.has_epsila_derivation(first_value):
            break
          else:
            first_set.remove(epsila)
        else:
          raise ValueError('Invalid literal: no terminal or non-terminal or epsila')
    r =  list(first_set)
    self.first[g_symbol] = r
    return r

  def calculate_follow(self, symbol, called_by = []):
    # Calculates Follow of the symbol. Returns a list of symbols and also 
    # places it in follow dict. List called_by is used to ensure that if
    # follow has already been calculated previously, it won't be calculated
    # again -- to avoid infinite recursion.

    follow_set = set()

    if symbol == self.grammar.grammar[0].non_terminal:
      follow_set.add(marker) 

    for production in self.grammar.grammar:
      if symbol in production.production:
        alpha_index = production.production.index(symbol)
        next_index = alpha_index + 1

        while(True):
          if next_index >= len(production.production):
            if not production.non_terminal in called_by and production.non_terminal != symbol:
              follow_set.update(self.calculate_follow(production.non_terminal, called_by + [symbol]))
            break

          elif production.production[next_index].symbol in self.grammar.terminals:
            follow_set.add(production.production[next_index].symbol)
            # check if the symbol exists in remaining production symbols.
            # if yes, continue to generate follow from that index.
            if symbol not in production.production[next_index:]:
              break
            else:
              next_index += production.production[next_index:].index(symbol)

          elif production.production[next_index].symbol in \
               self.grammar.non_terminals:
            follow_set.update(self.calculate_first(\
              production.production[next_index].symbol))
            if not self.has_epsila_derivation(\
              production.production[next_index].symbol):
              if symbol not in production.production[next_index:]:
                break
              else:
                next_index += production.production[next_index:]\
                .index(symbol)
          next_index += 1
    try:
      follow_set.remove(epsila)
    except KeyError:
      pass

    r =  list(follow_set)
    self.follow[symbol] = r
    
    return r

  def display(self):
    print "\n## First and Follow Calculation\n"
    for key, value in self.first.iteritems():
      print "First[%s] = %s" %(key, value)
    # print self.first
    print ""
    for key, value in self.follow.iteritems():
      print "Follow[%s] = %s" %(key, value)
    print "\n"


def main():
  from Grammar import Grammar

  grammar = """
  S' := S
  S := A c A
  S := B c c B
  A := c A
  A := a
  B := c c B
  B := b
  """

  grammar = """
S' := S
S := q A B C
A := a | b b D
B := a | E
C := b | E
D := C | E
"""

#   grammar = """
# S := a S a | b S b | D
# D := b D'
# D' := a a D' | E

# #   """

#   grammar = """
#   S := i X t S S' | a
#   S' := e S | E
#   X := b
#   """

  g = Grammar(grammar)
  g.parse()

  print g.first_follow.first
  print g.first_follow.follow
  # f = First_Follow(g)
  # # print f.calculate_first("B")

  # print f.first
  # print f.follow

if __name__ == '__main__':
  main()
