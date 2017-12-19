'''
January 27, 2016
'''

import copy

epsila = "E"
MAX_LOOP = 30

DEBUG = False

class Goto(object):
  '''Holds the list of productions produced by the goto function.'''

  def __init__(self, productions, closure, parent_goto, id):

    # List of productions in the Goto set.
    self.productions = productions

    self.parent_goto = parent_goto

    # symbol by which closure is generated.
    self.closure = closure

    self.id = id


  def __eq__(self, other):
    # Two Gotos are equal when every production in a goto matches the
    # productions in other Goto.
    if len(self.productions) != len(other.productions): return False
    for production in self.productions:
      if production not in other.productions: return False
    return True

  def has_production(self, searched_production):
    for production in self.productions:
      if production == searched_production:
        return True

  def __str__(self):
    return "GOTO[" + str(self.parent_goto) + ", " + \
            str(self.closure) + "] => " + str(self.id)

class GotoGenerator(object):
  """Generates Goto of a given grammar."""

  def __init__(self, grammar):
    super(GotoGenerator, self).__init__()

    self.grammar = grammar

    # Expected id for the next Goto function. It is incremented at every step
    # but if duplicate productions are found in previous gotos, the number is
    # again decremented.
    self.expected_id = 0


    # List of Gotos produced from the grammar.
    self.gotos = []
    # self.first_closure = Goto(self.grammar.grammar, "S", None, 0)

    r = [self.grammar.grammar[0]]
    self.recursive_non_terminal_lookup(r[0], r)

    # self.first_closure = self.get_goto(self.grammar.grammar, "S", 0)

    self.first_closure = Goto(r, "", None, 0)

    # self.first_closure = Goto(self.grammar.grammar, "", None, 0)

    self.goto_dict = {}


  def get_symbols_after_dot(self, productions):
    # Returns a list of symbols after dot from productions in a sequential
    # way. Duplicate symbols are not added.
    symbols_after_dot = []
    for production in productions:
      next_symbol = production.next_symbol()
      if next_symbol and next_symbol not in symbols_after_dot:
        symbols_after_dot.append(next_symbol)

      if DEBUG == True: print ">>>> " , production

    if DEBUG == True:
      rr = "\n["
      for j in symbols_after_dot: rr += str(j) + " "
      print rr + "]"
    return symbols_after_dot

  def generate(self):
    # Generate Gotos and its productions from the given grammar.

    # Start with the given grammar.
    # productions = self.grammar.grammar
    productions = self.first_closure.productions

    # closure_0 = Goto(productions, "", None, 0)
    # self.gotos.append(closure_0)

    gotos_index = 0
    parent_goto = 0
    prev_parent_goto = 0

    while True:
      symbols_after_dot = self.get_symbols_after_dot(productions)

      for symbol in symbols_after_dot:
        # NOTE: Goto sequence number should never decrease.
        if parent_goto >= prev_parent_goto:
          # Generate goto sequence from productions.
          new_goto = self.get_goto(productions, symbol, parent_goto)
          self.gotos.append(new_goto)

      if gotos_index >= len(self.gotos):
        # When there are no more gotos, end the loop.
        break

      # Next set of productions are from the calculated gotos.
      productions = self.gotos[gotos_index].productions

      if parent_goto >= prev_parent_goto: prev_parent_goto = parent_goto

      parent_goto = self.gotos[gotos_index].id
      gotos_index += 1

      if gotos_index > MAX_LOOP:
        print "ERROR: MAX LOOP EXCEEDED."
        break

    self.fill_goto_dict()


  def fill_goto_dict(self):
    for goto in self.gotos:
      self.goto_dict[str(goto.parent_goto) + str(goto.closure)] = goto

  def get_goto(self, productions, symbol, parent_goto):
    # Generates goto sequence from given productions.
    # E.g. if we have to calculate GOTO[1, s], then 
    #   symbol = s
    #   parent_goto = 1

    r = []
    for production in productions:
      if production.next_symbol() == symbol:
        new_production = copy.copy(production)
        new_production.increment_dot()
        r.append(new_production)

    # Check for non-terminal after dot.
    for production in r:
      self.recursive_non_terminal_lookup(production, r)

    # Check for duplicate goto. If so, decrement expected id.
    self.expected_id += 1
    r_goto = Goto(r, symbol, parent_goto, self.expected_id)
    for goto in self.gotos:
      if r_goto == goto:
        r_goto.id = goto.id
        self.expected_id -= 1
        break
    return r_goto

  def recursive_non_terminal_lookup(self, given_production, r):
    # If the production has non terminal after dot, list all the productions
    # of the terminal recursively and appends it to r

    # List of productions to be recursively checked.
    rec_productions = []
    if given_production.is_next_terminal() == False:
      for production in self.grammar.grammar:
        if production.non_terminal == given_production.next_symbol().symbol and production not in r:
          rec_productions.append(production)
          if production not in r: r.append(production)

    for production in rec_productions:
      self.recursive_non_terminal_lookup(production, r)

  def display(self):
    print self.first_closure
    for production in self.first_closure.productions:
      print production


    for goto in self.gotos:
      print goto
      for production in goto.productions:
        print production
      print ""

  def find_production(self, production):
    r = []

    if self.first_closure.has_production(production):
      r.append(self.first_closure)

    r += [goto for goto in self.gotos if goto.has_production(production)]

    return r
