'''
Grammar class

Note: Make sure that each word in raw is separated by a space

January 27, 2016
'''

import copy
from Production import ProductionGenerator, Production
from First_Follow import First_Follow

class Grammar(object):
  def __init__(self, raw):
    # Raw grammar.
    self.raw = raw

    # Following are calculated during parse.

    # Parsed grammar.
    self.grammar = []

    self.non_terminals = []
    self.terminals = []

    self.first_follow = None

  def parse(self):
    for line in self.raw.split("\n"):
      if line.find(":=") < 0: continue

      # Raw production may have splitter "|". So, it is split into multiple
      # productions to generate a list.
      ps = ProductionGenerator(line, self).generate()

      # Differentiate terminals and non terminals and place in 
      # respective arrays.
      for p in ps:
        self.grammar.append(p)
        for symbol in p.production:
          if symbol.symbol not in self.terminals:
            self.terminals.append(symbol.symbol)
        if p.non_terminal not in self.non_terminals:
          self.non_terminals.append(p.non_terminal)
    
    for symbol in self.non_terminals:
      if symbol in self.terminals: self.terminals.remove(symbol)

    self.first_follow = First_Follow(self)


  def __str__(self):
    r = ""
    for production in self.grammar:
      r += str(production) + "\n"
    return r

  def get(self, non_terminal):
    # returns a list of productions that has given non terminal.
    for production in self.grammar:
      if production.non_terminal == non_terminal:
        yield production


  def get_dot_terminal_productions(self):
    # returns productions that hat dot before terminal.
    # used for shifting.
    r = []
    for production in self.grammar:
      # print ">>>", production
      dot_indices = [i for i, symbol in enumerate(production.production) if symbol.symbol in self.terminals]
      for index in dot_indices:
        new_production = copy.copy(production)
        new_production.dot = index
        r.append(new_production)

    print "\nList of Productions that has dot before terminals:"
    for production in r:
      print production
    return r

  def get_alpha_dot_productions(self):
    # returns proudctions that has dot at the end.
    r = []
    for production in self.grammar:
      # if len(production.production):
        new_production = copy.copy(production)
        new_production.dot = len(new_production.production)
        r.append(new_production)

    print "\nList of Productions with dot at the end:"
    for production in r:
      print production
    return r

